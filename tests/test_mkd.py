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
    assert config.get("system.version") == "0.1.0"
    assert config.get("runtime.mode") == "development"
    assert config.get("runtime.debug") is True


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


def test_display():
    from core.display import Display

    display = Display(10, 10)

    assert display.to_dict() == {
        "version": "0.1.0",
        "width": 10,
        "height": 10,
    }

    display.set_pixel(2, 3, 255)

    assert display.get_pixel(2, 3) == 255

    display.clear()

    assert display.get_pixel(2, 3) == 0


def test_display_validation():
    from core.display import Display

    display = Display(10, 10)

    try:
        display.set_pixel(-1, 0, 255)
    except ValueError:
        pass
    else:
        raise AssertionError("Negative coordinate should fail")

    try:
        display.set_pixel(10, 0, 255)
    except ValueError:
        pass
    else:
        raise AssertionError("Width boundary should fail")

    try:
        Display(0, 10)
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid dimensions should fail")

def test_display_line():
    from core.display import Display

    display = Display(10, 10)

    display.draw_line(0, 0, 9, 9, 255)

    assert display.get_pixel(0, 0) == 255
    assert display.get_pixel(5, 5) == 255
    assert display.get_pixel(9, 9) == 255
    assert display.get_pixel(5, 0) == 0


def test_window_manager():
    from core.window import Window
    from core.window_manager import WindowManager

    manager = WindowManager()

    window = Window(
        10,
        20,
        300,
        200,
        "MKD Desktop"
    )

    window_id = manager.create_window(window)

    assert window_id == 1
    assert manager.get_window(window_id) is window
    assert manager.list_windows() == [1]
    assert manager.get_active_window() is window

    assert manager.set_active_window(window_id) is True
    assert manager.destroy_window(window_id) is True
    assert manager.get_window(window_id) is None
    assert manager.list_windows() == []


def test_desktop_composition():
    from core.display import Display
    from core.window_manager import WindowManager
    from core.desktop import Desktop

    display = Display(640, 480)
    manager = WindowManager()
    desktop = Desktop(display, manager)

    window_id = desktop.create_window(
        50, 50, 300, 200, "MKD Desktop"
    )

    assert window_id == 1
    assert desktop.list_windows() == [1]

    active = desktop.get_active_window()
    assert active is not None
    assert active.title == "MKD Desktop"

    info = desktop.to_dict()
    assert info["version"] == "0.1.1"
    assert info["display"]["width"] == 640
    assert info["display"]["height"] == 480
    assert info["window_manager"]["window_count"] == 1

    return True
