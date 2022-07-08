# National Weather Service Console Application in Python

### Overview
- Python3 console program using requests, National Weather Service API and Nominatim from geopy.
- Includes current, forecast weather, and weather alerts.
- The lat and long are retrieved using Nominatim from geopy.
- JSON sample response files used to build the program are in the json_response_files folder.
- A batch file is included for using nuitka to build to a Windows exe (nuitka_console.bat)
    * Install nuitka: pip install nuitka

### Changes
- 09/17/2021: Initial commit
- 11/28/2021: Make nws_class less console specific to be able to be used in any other programs

### License
<a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License</a>.

Copyright (c) 2022 William A Loring

