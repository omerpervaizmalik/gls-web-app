@echo off
echo ======================================================
echo    GET LEGAL SOLUTION - MASTER STATUTORY PORTAL
echo ======================================================
echo.
echo Starting the High-Speed Statutory Library Server...
echo.

:: Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is required but not found. 
    echo Please install Python to enable the full library.
    pause
    exit /b
)

:: Inform the user
echo [INFO] Library initializing on http://localhost:8080
echo [INFO] Opening your Premium Statutory Records...
echo.

:: Start the Python server in the background
start /b python -m http.server 8080

:: Wait a moment for server to start
timeout /t 2 /nobreak >nul

:: Open the relevant laws page
start http://localhost:8080/relevant-laws.html

echo [SUCCESS] Portal is now active. 
echo You can now read the 100% Real Statutory Text for all 52 laws.
echo Keep this window open while you browse.
echo.
echo Press any key to stop the server and close.
pause >nul

:: Kill the python server process on exit
taskkill /f /im python.exe >nul 2>&1
exit
