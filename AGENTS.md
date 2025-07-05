# Notice
This project is for personal, local use on Windows 11 and is **not** intended for production scale.

# Agents

## FrameLoader
Responsibility: Load and validate exactly three keyframe image files.

## FLF2VInterpolator
Responsibility: Use the Wan2.1 FLF2V model to interpolate video segments between keyframes.

## VideoStitcher
Responsibility: Stitch the two generated segments into a single video using MoviePy.

## GUIController
Responsibility: Provide a minimal Tkinter GUI for:
- Selecting three image files
- Triggering the generation process
- Previewing and saving the output video

## ConfigAgent
Responsibility: Parse and apply configuration options:
- `output_path`
- `frame_rate`
- `video_codec`

# Configuration Options
- **output_path**: Path to save the generated video file.
- **frame_rate**: Frames per second for the output video.
- **video_codec**: Codec used for encoding the video (e.g., `mp4v`).
