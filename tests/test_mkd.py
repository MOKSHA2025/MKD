from core import (
    MKDCore,
    create_event,
    Config,
    get_logger,
    MKDRuntimeError,
)


def test_event():
    event = create_event("keyboard", {"key": "A"})

    assert event.to_dict() == {
        "type": "keyboard",
        "data": {"key": "A"},
    }


def test_config():
    config = Config()

    assert config.get("system.name") == "MOKSHA KERNEL DESKTOP EXPERIMENT"
    assert config.has("display.theme")


def test_runtime():
    core = MKDCore()

    assert core.status()["runtime"] == "stopped"
    assert core.start() is True
    assert core.status()["runtime"] == "running"
    assert core.stop() is True
    assert core.status()["runtime"] == "stopped"


def test_event_queue():
    core = MKDCore()
    received = []

    core.events.register(
        "keyboard",
        lambda event: received.append(event.to_dict())
    )

    core.start()

    core.queue_event(
        create_event("keyboard", {"key": "A"})
    )

    assert core.pending_events() == 1
    assert core.process_events() == 1

    assert received == [
        {
            "type": "keyboard",
            "data": {"key": "A"},
        }
    ]

    core.stop()


def test_error_handling():
    core = MKDCore()

    try:
        core.queue_event(
            create_event("keyboard", {"key": "A"})
        )
    except MKDRuntimeError as error:
        assert error.to_dict()["type"] == "MKDRuntimeError"
    else:
        raise AssertionError("Expected MKDRuntimeError")


def test_logger():
    logger = get_logger("TEST")

    assert logger.name == "TEST"
