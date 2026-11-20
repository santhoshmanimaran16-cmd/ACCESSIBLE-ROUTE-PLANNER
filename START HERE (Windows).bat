@echo off
cd /d "%~dp0"
where python >nul 2>nul && (python start_app.py & goto :eof)
where py >nul 2>nul && (py start_app.py & goto :eof)
echo Python is not installed. Get it from https://www.python.org/downloads/ (tick "Add Python to PATH"), then run this again.
pause
