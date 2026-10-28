@echo off
title FINCH-ZK — LLM Hallucination Detection
echo.
echo  ==========================================
echo   FINCH-ZK  Hallucination Detection App
echo  ==========================================
echo.

REM Check for .env file
if not exist .env (
    echo  [!] .env file not found.
    echo      Copying .env.example to .env ...
    copy .env.example .env >nul
    echo.
    echo  [!] Please open .env and add your API keys, then re-run this script.
    echo      ANTHROPIC_API_KEY = your Anthropic key  (console.anthropic.com)
    echo      GROQ_API_KEY      = your Groq key       (console.groq.com)
    echo.
    pause
    start notepad .env
    exit /b 1
)

REM Install dependencies if needed
echo  [*] Checking dependencies ...
pip install -r requirements.txt --quiet

echo.
echo  [*] Starting Flask server on http://localhost:5000
echo      Login: admin / admin
echo      Press Ctrl+C to stop.
echo.
python app.py
pause

