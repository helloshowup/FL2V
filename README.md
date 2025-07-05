# FLF2V Demo Video Generator

Generate a 5-second demo video from three key-frame images using the Wan 2.1 FLF2V model on Windows 11. For personal experimentation only—**not** production scale.

## Prerequisites

- Windows 11
- Python 3.10 or later
- Git (optional)

## Installation

1. Clone or download the repo:
   ```bash
   git clone https://github.com/your-username/FLF2V.git
   cd FLF2V
Create and activate a virtual environment:

bash
Copy
Edit
python -m venv venv
venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Alternatively, run the bundled script:

bat
Copy
Edit
run.bat
That creates the venv, installs requirements and launches the GUI.

Usage
Command-Line
bash
Copy
Edit
python main.py --frames frame1.png frame2.png frame3.png
GUI
Run:

bash
Copy
Edit
python main.py
In the Tkinter window:

Select exactly three key-frame images.

Click Generate.

Preview the 5-second video.

Save to a custom path (default: sample_output.mp4).

Sample Keyframes
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

GUIController
Minimal Tkinter interface for file selection and preview.

ConfigAgent
Parse and apply output path, frame rate and codec settings.


## Tests

Run the unit tests with:

```bash
python -m unittest discover -s tests -v
```

The tests require OpenCV, NumPy and MoviePy.

Keep it simple. No fluff.