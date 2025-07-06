import os
import sys
import tempfile
import unittest

import cv2
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from frame_loader import FrameLoader


class TestFrameLoader(unittest.TestCase):
    def create_dummy_image(self, path, size=(1024, 1024)):
        img = np.zeros((size[0], size[1], 3), dtype=np.uint8)
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
                self.assertEqual(f.shape[:2], (1024, 1024))

    def test_invalid_extension_raises(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            p = os.path.join(tmpdir, "img.jpg")
            self.create_dummy_image(p)
            with self.assertRaises(ValueError):
                FrameLoader.load_frames([p, p, p])

    def test_invalid_size_raises(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            p = os.path.join(tmpdir, "img.png")
            self.create_dummy_image(p, size=(512, 512))
            with self.assertRaises(ValueError):
                FrameLoader.load_frames([p, p, p])


if __name__ == "__main__":
    unittest.main()
