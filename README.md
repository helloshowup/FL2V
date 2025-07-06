# FLF2V Demo Video Generator

Generate a 5-second demo video from three key-frame images using the Wan 2.1 FLF2V model on Windows 11. For personal experimentation only—**not** production scale.

## Prerequisites

- Windows 11
- Python 3.10 or later
- Git (optional)

## Installation

1. Clone or download the repo and create a virtual environment:
   ```bash
   git clone https://github.com/your-username/FLF2V.git
   cd FLF2V
   python -m venv venv
   venv\Scripts\activate
   ```
2. Install the base requirements and Wan2.1:
   ```bash
   pip install -r requirements.txt
   git clone https://github.com/Wan-Video/Wan2.1.git
   # Install PyTorch first (replace cu118 with your CUDA version)
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   # Install Wan2.1 requirements after PyTorch so flash-attn can build
   pip install --find-links deps --no-build-isolation -r Wan2.1\requirements.txt
   pip install -e Wan2.1
   ```
   The `Wan2.1` directory is git-ignored so cloned files won't be committed.
3. Alternatively, run the bundled script:
   ```
   run.bat
   ```
   The script creates the venv, installs requirements (including PyTorch and flash-attn) and launches the GUI. It checks the `deps` folder for PyTorch or flash-attn wheels before downloading from PyPI and pauses on error so you can read the message.

## Usage

### GUI
```bash
python main.py
```
In the Tkinter window:

- Select exactly three key-frame images.
- Click **Generate**.
- Preview the 5-second video.
- Save to a custom path (default: `sample_output.mp4`).

## Sample Keyframes
Provide exactly three PNG images sized 1024x1024 pixels (start, midpoint and end frames) in the `sample_images/` folder. The loader rejects images that are not PNG or not 1024x1024.

Output
Default: sample_output.mp4

~5 seconds at 24 fps (configurable via --frame_rate or GUI settings).
The output video always has a 1:1 aspect ratio.

Codec and output path can be changed in config.ini or via CLI flags.

Configuration
Option	CLI flag	Default
Output path	--output_path PATH	sample_output.mp4
Frame rate	--frame_rate FPS	24
Video codec	--video_codec CODEC	libx264

Components
FrameLoader
Load and validate exactly three key-frame images.

FLF2VInterpolator
Interpolate frames with the Wan 2.1 FLF2V model.

VideoStitcher
Stitch interpolated frames into a video using MoviePy.