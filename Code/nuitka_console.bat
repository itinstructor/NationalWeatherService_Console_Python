cd c:\temp

python -m nuitka ^
    --onefile ^
    --windows-icon-from-ico=weather.ico ^
    nws_console.py
pause