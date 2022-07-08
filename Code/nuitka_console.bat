cd c:\temp

python -m nuitka ^
    --onefile ^
    --disable-ccache ^
    --windows-icon-from-ico=weather.ico ^
    nws_console.py
pause