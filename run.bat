@echo off

python -m venv venv || goto :error
call venv\Scripts\activate || goto :error

:: Clone Wan2.1 if it isn't already present
if not exist Wan2.1 (git clone https://github.com/Wan-Video/Wan2.1.git) || goto :error

:: Install Wan2.1 and project requirements
pip install -r Wan2.1\requirements.txt || goto :error
pip install -e Wan2.1 || goto :error
pip install -r requirements.txt || goto :error

:: ---- PyTorch and flash-attn ----
:: Install PyTorch from local wheels if available, otherwise use the official index
if exist deps\torch*.whl (
    pip install deps\torch*.whl deps\torchvision*.whl deps\torchaudio*.whl || goto :error
) else (
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 || goto :error
)

:: Install flash-attn after PyTorch. Use local wheel if provided
if exist deps\flash_attn*.whl (
    pip install deps\flash_attn*.whl || goto :error
) else (
    pip install flash-attn --no-build-isolation || goto :error
)

python main.py || goto :error

exit /b 0

:error
echo Launch failed. See above for details. > error.log
pause
exit /b 1
