import json
import os
import tempfile
import unittest

from config_agent import ConfigAgent


class TestConfigAgent(unittest.TestCase):
    def test_defaults(self):
        cfg = ConfigAgent()
        self.assertEqual(cfg.get_output_path(), "output.mp4")
        self.assertEqual(cfg.get_frame_rate(), 24)
        self.assertEqual(cfg.get_video_codec(), "libx264")

    def test_config_file_override(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "cfg.json")
            with open(path, "w", encoding="utf-8") as f:
                json.dump({"output_path": "out.mp4", "frame_rate": 30, "video_codec": "h264"}, f)
            cfg = ConfigAgent(config_path=path)
            self.assertEqual(cfg.get_output_path(), "out.mp4")
            self.assertEqual(cfg.get_frame_rate(), 30)
            self.assertEqual(cfg.get_video_codec(), "h264")


if __name__ == "__main__":
    unittest.main()
