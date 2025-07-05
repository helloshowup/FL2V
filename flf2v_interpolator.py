import logging
from typing import List

import cv2

try:
    from wan import FLF2V
except ImportError:  # pragma: no cover - wan library may not be installed in CI
    FLF2V = None


class FLF2VInterpolator:
    """Interpolate video segments between keyframes using Wan2.1 FLF2V model."""

    def __init__(self):
        if FLF2V is None:
            raise ImportError("wan library with FLF2V model is required")
        logging.info("Loading Wan2.1 model...")
        self.model = FLF2V.from_pretrained("wan2.1")
        logging.info("Model loaded")

    def interpolate(self, frames: List, frame_rate: int) -> List[List]:
        """Generate intermediate clips between frames.

        Parameters
        ----------
        frames: list
            Three keyframe images as numpy arrays.
        frame_rate: int
            Desired frame rate for output video.

        Returns
        -------
        list of list
            Two lists of interpolated frames corresponding to the segments
            between frame[0]-frame[1] and frame[1]-frame[2].
        """
        if len(frames) != 3:
            raise ValueError("Exactly three frames are required")

        total_frames = frame_rate * 5
        segment_frames = total_frames // 2
        clips: List[List] = []

        for i in range(2):
            start, end = frames[i], frames[i + 1]
            logging.info("Interpolating segment %d", i + 1)
            # Placeholder interpolation using simple linear blending
            segment = []
            for f in range(segment_frames):
                alpha = f / (segment_frames - 1) if segment_frames > 1 else 0
                inter = cv2.addWeighted(start, 1 - alpha, end, alpha, 0)
                segment.append(inter)
            clips.append(segment)
            logging.info("Segment %d complete", i + 1)

        return clips
