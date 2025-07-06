# Dockerfile
FROM nvidia/cuda:11.8.0-cudnn8-runtime-ubuntu22.04

# 1) System deps
RUN apt-get update && apt-get install -y \
    python3.10 python3.10-venv python3-pip git cmake ninja-build \
 && rm -rf /var/lib/apt/lists/*

# 2) Create & activate venv
WORKDIR /workspace
RUN python3.10 -m venv venv
ENV PATH="/workspace/venv/bin:${PATH}"

# 3) Install Python deps
COPY requirements.txt /workspace/requirements.txt
RUN pip install --upgrade pip \
 && pip install --extra-index-url https://download.pytorch.org/whl/cu118 \
      torch==2.7.1+cu118 torchvision==0.15.2+cu118 torchaudio==2.7.2+cu118 \
 && pip install -r requirements.txt

# 4) Clone & install Wan2.1
RUN git clone https://github.com/Wan-Video/Wan2.1.git
RUN pip install --no-build-isolation -r Wan2.1/requirements.txt \
 && pip install -e Wan2.1

# 5) Add your FLF2V code and entrypoint
COPY . /workspace/FLF2V
WORKDIR /workspace/FLF2V
ENTRYPOINT ["python", "main.py"]
