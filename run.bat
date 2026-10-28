@echo off
title FINCH-ZK — LLM Hallucination Detection & Mitigation Platform
cls
color 0B
echo.
echo  =============================================================================
echo    [+] FINCH-ZK v2.4 Enterprise Platform
echo    LLM Hallucination Detection and Mitigation (Group 11 - 2026)
echo    Vidya Academy of Science and Technology, Thrissur
echo  =============================================================================
echo.

REM 1. Ensure .env exists without blocking
if not exist .env (
    echo  [*] Initializing environment configuration...
    if exist .env.example (
        copy .env.example .env >nul
    ) else (
        echo FLASK_SECRET_KEY=finch-zk-group11-2026-secret > .env
    )
)

REM 2. Install dependencies silently if needed
echo  [*] Checking dependencies (Flask, PySBD, Anthropic, Requests)...
python -m pip install -r requirements.txt --quiet --disable-pip-version-check

echo.
echo  [*] Starting FINCH-ZK Platform on http://localhost:5000 ...
echo      Admin Credentials:
echo        - Username: admin
echo        - Password: admin
echo.
echo  [*] Opening your browser automatically in 2 seconds...
echo      (Press Ctrl+C in this window anytime to stop the server)
echo.

REM 3. Trigger browser opener in background
start "" cmd /c "timeout /t 2 /nobreak >nul & start http://localhost:5000"

REM 4. Launch Flask Application
python app.py

pause
