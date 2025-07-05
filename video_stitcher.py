import logging
from typing import List

try:
    import moviepy.editor as mpy  # MoviePy <2.2.0
except Exception:  # pragma: no cover - fallback for newer MoviePy versions
    import moviepy as mpy


class VideoStitcher:
    """Stitch interpolated clips into a final video."""

    def __init__(self, codec: str = "libx264"):
        self.codec = codec

    def stitch(self, clips: List[List], output_path: str, frame_rate: int) -> str:
        """Concatenate clips and write to a video file.

        Parameters
        ----------
        clips : List[List]
            List of frame sequences (each a list of numpy arrays).
        output_path : str
            Path to write the final video.
        frame_rate : int
            Frame rate for the output video.

        Returns
        -------
        str
            Path to the generated video file.
        """
        if not clips:
            raise ValueError("No clips provided for stitching")

        logging.info("Stitching %d clips", len(clips))
        video_clips = []
        for idx, frames in enumerate(clips):
            if not frames:
                continue
            logging.info("Creating subclip %d with %d frames", idx + 1, len(frames))
            subclip = mpy.ImageSequenceClip(frames, fps=frame_rate)
            video_clips.append(subclip)

        if not video_clips:
            raise ValueError("All provided clips were empty")

        final = mpy.concatenate_videoclips(video_clips)
        logging.info("Writing output video to %s", output_path)
        final.write_videofile(output_path, codec=self.codec, fps=frame_rate, audio=False)
        logging.info("Video written successfully")
        return output_path
