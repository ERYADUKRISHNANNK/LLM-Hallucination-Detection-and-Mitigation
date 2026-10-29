@echo off
cd /d "%~dp0"
title FINCH-ZK LLM Hallucination Detection and Mitigation

echo.
echo  =============================================================================
echo    [+] FINCH-ZK v2.4 Enterprise Platform
echo    LLM Hallucination Detection and Mitigation (Group 11 - 2026)
echo    Vidya Academy of Science and Technology, Thrissur
echo  =============================================================================
echo.

:: 1. Detect Python
set PY_CMD=python
python --version >nul 2>&1
if errorlevel 1 (
    py --version >nul 2>&1
    if not errorlevel 1 (
        set PY_CMD=py
    ) else if exist "%LOCALAPPDATA%\Programs\Python\Python313\python.exe" (
        set "PY_CMD=%LOCALAPPDATA%\Programs\Python\Python313\python.exe"
    ) else (
        echo [ERROR] Python was not found on your system!
        echo         Please install Python 3.10+ from https://python.org
        echo         Ensure "Add Python to PATH" is checked during installation.
        pause
        exit /b 1
    )
)

echo  [*] Python interpreter: %PY_CMD%

:: 2. Ensure .env exists
if not exist .env (
    echo  [*] Initializing default .env configuration...
    if exist .env.example (
        copy .env.example .env >nul
    ) else (
        echo FLASK_SECRET_KEY=finch-zk-group11-2026-secret > .env
    )
)

:: 3. Fast dependency check
echo  [*] Checking dependencies (Flask, PySBD, Anthropic, Requests)...
%PY_CMD% -c "import flask, pysbd, anthropic, requests" >nul 2>&1
if errorlevel 1 (
    echo  [*] Installing required dependencies from requirements.txt...
    %PY_CMD% -m pip install -r requirements.txt --disable-pip-version-check
) else (
    echo  [*] All dependencies are verified and ready.
)

echo.
echo  [*] Starting FINCH-ZK Platform...
echo      - Dashboard URL: http://localhost:5000
echo      - Login user:    admin
echo      - Login pass:    admin
echo.
echo  [*] Opening your browser automatically once the server is listening...
echo      (Press Ctrl+C anytime in this window to stop the server)
echo.

:: 4. Start Flask App
%PY_CMD% app.py

echo.
echo  [!] Server stopped.
pause
