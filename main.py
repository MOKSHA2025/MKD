from core import MKDCore, Config, get_logger

def main():
    print("======================================")
    print("   MOKSHA KERNEL DESKTOP EXPERIMENT")
    print("======================================")

    logger = get_logger("MKD-BOOT")
    config = Config()
    core = MKDCore()

    print("[MKD] Configuration loaded")
    print("[MKD] Core initialized")
    print("[MKD] MKD Foundation ready")

    core.start()

    print("[MKD] Runtime started")
    print("[MKD] MKD BOOT COMPLETE")

    core.stop()

    print("[MKD] Runtime stopped")
    print("[MKD] Shutdown complete")


if __name__ == "__main__":
    main()
