import json
import os


class ConfigAgent:
    """Parse configuration options for the FLF2V workflow."""

    DEFAULTS = {
        "output_path": "sample_output.mp4",
        "frame_rate": 24,
        "video_codec": "libx264",
    }

    def __init__(self, config_path: str | None = None, overrides: dict | None = None):
        config = dict(self.DEFAULTS)

        if config_path and os.path.exists(config_path):
            with open(config_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, dict):
                    for key in self.DEFAULTS:
                        if key in data:
                            config[key] = data[key]
                else:
                    raise ValueError("Config file must contain a JSON object")

        if overrides:
            for key in self.DEFAULTS:
                if key in overrides:
                    config[key] = overrides[key]

        self.output_path = config["output_path"]
        self.frame_rate = config["frame_rate"]
        self.video_codec = config["video_codec"]

    def get_output_path(self) -> str:
        return self.output_path

    def get_frame_rate(self) -> int:
        return self.frame_rate

    def get_video_codec(self) -> str:
        return self.video_codec
