@echo off
setlocal
cd /d "%~dp0"
set PORT=4173
set URL=http://127.0.0.1:%PORT%/gallery.html

echo Starting Family Gallery server on %URL%
echo Keep this window open while using the gallery.
echo Press Ctrl+C to stop the server.

start "" cmd /c "timeout /t 2 /nobreak >nul && start \"\" \"%URL%\""

where py >nul 2>nul
if %errorlevel%==0 (
    py gallery_server.py --port %PORT%
    goto :eof
)

where python >nul 2>nul
if %errorlevel%==0 (
    python gallery_server.py --port %PORT%
    goto :eof
)

echo.
echo Python was not found. Install Python 3 and try again.
pause
exit /b 1
