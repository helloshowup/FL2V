@echo off

python -m venv venv || goto :error
call venv\Scripts\activate || goto :error
pip install -r requirements.txt || goto :error
python main.py || goto :error

exit /b 0

:error
echo launch terminal > error.log
exit /b 1
