import logging
from config_agent import ConfigAgent
from gui_controller import GUIController


def main():
    """Entry point for the FLF2V application."""
    logging.basicConfig(level=logging.INFO)
    cfg = ConfigAgent(
        overrides={
            "output_path": "sample_output.mp4",
            "frame_rate": 24,
            "video_codec": "mp4v",
        }
    )
    gui = GUIController(cfg)
    gui.run()


if __name__ == "__main__":
    main()

