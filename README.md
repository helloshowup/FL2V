# FL2V

This project demonstrates a simple First-Last-Frame-to-Video (FLF2V) workflow using the Wan 2.1 model. It is intended for personal experimentation on Windows 11.

## Setup

1. Ensure Python 3.10 or later is installed.
2. Run `run.bat` to create a virtual environment, install dependencies from `requirements.txt`, and launch the GUI.

Alternatively, perform the steps manually:

```bat
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Sample Keyframes

Place or create three images illustrating a simple physical-education movement (for example, start, midpoint and end of a sit-up) in the folder `sample_images/`. The program expects exactly three images.

## Running

Execute `python main.py` (or use `run.bat`). Select the three images when prompted. The application generates a roughly 5‑second video saved to `sample_output.mp4` by default. Open the output file to confirm it plays correctly.

## Tests

Unit tests cover the `FrameLoader` and `VideoStitcher` components. Run them with:

```bash
python -m unittest discover -s tests -v
```

The tests may fail if OpenCV, NumPy or MoviePy are not installed.
