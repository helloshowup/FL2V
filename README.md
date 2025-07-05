# FLF2V Demo Video Generator

This project is for personal, local use on Windows 11 and is **not** intended for production scale.

## Project Overview
Generate 5-second demo videos from three key frames using the Wan2.1 FLF2V model on Windows 11.

## Installation
- Python 3.8+
- pip

```bash
pip install wan moviepy tkinter
```

## Usage
Run from the command line:

```bash
python main.py --frames frame1.png frame2.png frame3.png
```

Minimal Tkinter GUI workflow:
1. Select three key frame images.
2. Trigger generation.
3. Preview the output video.
4. Save the result.

## Agents
- **FrameLoader**: Load and validate exactly three keyframe image files.
- **FLF2VInterpolator**: Use the Wan2.1 FLF2V model to interpolate video segments.
- **VideoStitcher**: Stitch segments into a single video using MoviePy.
- **GUIController**: Provide a minimal Tkinter GUI for input selection and output preview.
- **ConfigAgent**: Parse and apply `output_path`, `frame_rate`, and `video_codec`.
