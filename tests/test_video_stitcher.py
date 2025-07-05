import os
import tempfile
import unittest

import numpy as np

from video_stitcher import VideoStitcher

try:
    import moviepy
    MOVIEPY_AVAILABLE = True
except Exception:
    MOVIEPY_AVAILABLE = False


class TestVideoStitcher(unittest.TestCase):
    def create_dummy_clip(self, frame_count):
        frames = []
        for _ in range(frame_count):
            frames.append(np.zeros((8, 8, 3), dtype=np.uint8))
        return frames

    def test_stitch_creates_file(self):
        if not MOVIEPY_AVAILABLE:
            self.skipTest("moviepy not available")
        clips = [self.create_dummy_clip(3), self.create_dummy_clip(3)]
        stitcher = VideoStitcher()
        with tempfile.TemporaryDirectory() as tmpdir:
            out = os.path.join(tmpdir, "out.mp4")
            stitcher.stitch(clips, out, frame_rate=2)
            self.assertTrue(os.path.exists(out))


if __name__ == "__main__":
    unittest.main()
