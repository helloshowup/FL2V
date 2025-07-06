# FLF2V Demo Video Generator

Generate a 5-second demo video from three key-frame images using the Wan 2.1 FLF2V model on Windows 11. For personal experimentation only—**not** production scale.

## Prerequisites

- Windows 11 with Virtualization enabled
- WSL 2
- Docker Desktop (WSL 2 backend)
- NVIDIA GPU drivers


## Installation via Docker

```dockerfile
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04
RUN apt-get update && apt-get install -y python3.10-venv python3-pip git cmake ninja-build
WORKDIR /workspace
RUN python3.10 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install --index-url https://download.pytorch.org/whl/cu118 \
        torch==2.7.1+cu118 torchvision==0.15.2+cu118 torchaudio==2.7.2+cu118 && \
    pip install flash-attn
COPY . /workspace/FLF2V
WORKDIR /workspace/FLF2V
RUN . /workspace/venv/bin/activate && \
    pip install -r requirements.txt && \
    pip install wan  # install FLF2V model library if available
ENTRYPOINT ["python","main.py"]
```

```bash
docker build -t flf2v-demo .
```

```bash
docker run --gpus all -v /local/in:/workspace/in -v /local/out:/workspace/out flf2v-demo
```
## Legacy: Native Windows build

> **Warning**
> This method often fails on Windows and can take more than two hours. See [issue #1](https://github.com/your-username/FLF2V/issues/1) for details.

Use `run.bat` to build the virtual environment and install all dependencies.

### Legacy Troubleshooting

Below is a running list of issues we've encountered when building or running PyTorch and CUDA-enabled extensions on Windows using PowerShell. Add new items as needed.

1. **CUDA version mismatch**
   **Symptom:**
   ```
   RuntimeError: The detected CUDA version (12.9) mismatches the version that was used to compile PyTorch (11.8).
   ```
   **Fix:** Ensure the PyTorch wheel matches your installed CUDA Toolkit or rebuild PyTorch against the desired CUDA version.
   GPUs with compute capability 6.1 (GTX 1080 Ti) are not supported by the cu12.9 prebuilt wheels, so install the PyTorch `cu118` wheel instead.

2. **Missing Python YAML module**  
   **Symptom:**
   ```
   ModuleNotFoundError: No module named 'yaml'
   ```
   **Fix:**
   ```powershell
   pip install pyyaml
   ```

3. **Ninja build-backend not found**  
   **Symptom:**
   ```
   UserWarning: Attempted to use ninja as the BuildExtension backend but we could not find ninja.
   ```
   **Fix:**
   ```powershell
   pip install ninja
   ```

4. **CMake not available in venv**  
   **Symptom:**
   ```
   FileNotFoundError: [WinError 2] The system cannot find the file specified
   ```
   when CMake tries to invoke `ninja`.
   **Fix:**
   ```powershell
   pip install cmake
   ```

5. **Stale CMake cache or corrupted build folder**  
   **Symptom:** CMake repeatedly sees an old `CMakeCache.txt` referencing a missing `ninja.exe`.
   **Fix:**
   ```powershell
   Remove-Item -Recurse -Force .\build
   ```
   Then rebuild:
   ```powershell
   pip install -e . --no-build-isolation
   ```
## Usage


### GUI
```bash
python main.py
```
In the Tkinter window:

- Select exactly three key-frame PNG images.
- Click **Generate**.
- Preview the 5-second video.
- Save to a custom path (default: `/workspace/out/sample_output.mp4`).

## Sample Keyframes
Place exactly three 1024x1024 PNG images in `/workspace/in`. The loader rejects images that are not PNG or not 1024x1024.

Output
Default: `/workspace/out/sample_output.mp4`

~5 seconds at 24 fps (configurable via config.ini or GUI).
The output video always has a 1:1 aspect ratio.

Codec and output path can be changed in config.ini or via the GUI.

## Configuration
Option       Default
Output path  /workspace/out/sample_output.mp4
Frame rate   24
Video codec  libx264

Components
FrameLoader
Load and validate exactly three key-frame images.

FLF2VInterpolator
Interpolate frames with the Wan 2.1 FLF2V model.

VideoStitcher
Stitch interpolated frames into a video using MoviePy.


## Verify

```bash
docker run --rm hello-world
```

```bash
docker run --gpus all flf2v-demo python -c "import torch, flash_attn; print(torch.__version__, flash_attn.__version__)"
```
