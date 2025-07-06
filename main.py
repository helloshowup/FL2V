import logging
from config_agent import ConfigAgent
from gui_controller import GUIController


def main():
    """Entry point for the FLF2V application."""
    logging.basicConfig(level=logging.INFO)
    cfg = ConfigAgent()
    gui = GUIController(cfg)
    gui.run()


if __name__ == "__main__":
    main()

