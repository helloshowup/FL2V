@echo off

python -m venv venv || goto :error
call venv\Scripts\activate || goto :error
if not exist Wan2.1 (git clone https://github.com/Wan-Video/Wan2.1.git) || goto :error
pip install -r Wan2.1\requirements.txt || goto :error
pip install -e Wan2.1 || goto :error
pip install -r requirements.txt || goto :error
python main.py || goto :error

exit /b 0

:error
echo Launch failed. See above for details. > error.log
pause
exit /b 1
