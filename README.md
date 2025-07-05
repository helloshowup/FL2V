# FLF2V Demo Video Generator

Generate a short demo video from three key-frame images using the Wan 2.1 FLF2V model. This project is for personal use on Windows 11 and is **not** intended for production.

## Prerequisites

- Windows 11
- Python 3.10 or later
- Git (optional)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/FLF2V.git
   cd FLF2V
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies and the Wan2.1 model:
   ```bash
   pip install -r requirements.txt
   git clone https://github.com/Wan-Video/Wan2.1.git
   pip install -r Wan2.1\requirements.txt
   pip install -e Wan2.1
   # Install PyTorch before flash-attn (replace cu118 with your CUDA version)
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   pip install flash-attn --no-build-isolation
   ```
   The `Wan2.1` directory is git-ignored so cloned files are not committed.

Alternatively, run the bundled script:

```bash
run.bat
```

The script sets up the environment, installs requirements, clones Wan2.1 and then launches the GUI. If `deps` contains PyTorch or flash-attn wheels, the script uses them instead of downloading. It pauses on any error so you can read the message.

## Usage

### Command line

```bash
python main.py --frames frame1.png frame2.png frame3.png
```

### GUI

```bash
python main.py
```
1. Select exactly three key-frame images.
2. Click **Generate**.
3. Preview or save the output video (default: `sample_output.mp4`).

## Sample Keyframes

Provide three 1024x1024 PNG images (start, midpoint and end) in the `sample_images/` folder. Images of the wrong type or size are rejected.

## Output

- Default path: `sample_output.mp4`
- About 5 seconds at 24 fps (configurable via `--frame_rate` or GUI settings)
- Always 1:1 aspect ratio
- Codec and path can be changed in `config.ini` or via CLI flags.

## Configuration

| Option      | CLI flag              | Default             |
|-------------|----------------------|---------------------|
| Output path | `--output_path PATH` | `sample_output.mp4` |
| Frame rate  | `--frame_rate FPS`   | `24`                |
| Video codec | `--video_codec CODEC`| `libx264`           |

## Components

- **FrameLoader** – load and validate exactly three key-frame images.
- **FLF2VInterpolator** – interpolate frames with the Wan 2.1 FLF2V model.
- **VideoStitcher** – stitch interpolated frames into a video using MoviePy.
- **GUIController** – minimal Tkinter interface for file selection and preview.
- **ConfigAgent** – parse and apply output path, frame rate and codec settings.

## Tests

Run the unit tests with:

```bash
python -m unittest discover -s tests -v
```

The tests require OpenCV, NumPy and MoviePy. Errors raise exceptions rather than being ignored.

