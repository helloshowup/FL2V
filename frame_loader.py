import os
import cv2

class FrameLoader:
    """Load and validate exactly three keyframe images."""

    @staticmethod
    def load_frames(paths):
        if len(paths) != 3:
            raise ValueError("Exactly three frame paths required")

        frames = []
        for path in paths:
            ext = os.path.splitext(path)[1].lower()
            if ext != ".png":
                raise ValueError(f"Keyframe must be a PNG file: {path}")

            img = cv2.imread(path)
            if img is None:
                raise FileNotFoundError(f"Failed to load image: {path}")

            h, w = img.shape[:2]
            if h != 1024 or w != 1024:
                raise ValueError(
                    f"Keyframe must be 1024x1024 pixels: {path} is {w}x{h}"
                )

            frames.append(img)

        return frames
