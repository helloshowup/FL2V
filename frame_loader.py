import cv2

class FrameLoader:
    """Load and validate exactly three keyframe images."""

    @staticmethod
    def load_frames(paths):
        if len(paths) != 3:
            raise ValueError("Exactly three frame paths required")

        frames = []
        for path in paths:
            img = cv2.imread(path)
            if img is None:
                raise FileNotFoundError(f"Failed to load image: {path}")
            frames.append(img)

        return frames
