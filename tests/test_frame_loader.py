import os
import tempfile
import unittest

import cv2
import numpy as np

from frame_loader import FrameLoader


class TestFrameLoader(unittest.TestCase):
    def create_dummy_image(self, path):
        img = np.zeros((10, 10, 3), dtype=np.uint8)
        cv2.imwrite(path, img)

    def test_load_frames_three_images(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            paths = []
            for i in range(3):
                p = os.path.join(tmpdir, f"img{i}.png")
                self.create_dummy_image(p)
                paths.append(p)

            frames = FrameLoader.load_frames(paths)
            self.assertEqual(len(frames), 3)
            for f in frames:
                self.assertEqual(f.shape, (10, 10, 3))


if __name__ == "__main__":
    unittest.main()
