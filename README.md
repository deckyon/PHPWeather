# PHPWeather
Pull the information from my own PWS (Personal Weather Station) via Weather Underground and write it to a web page.

Hardware used/required: Onion Omega 2+, Onion Expansion Dock, Onion OLED Expansion.

You will also need to pick up your own API Key from Weather Underground at the following location: https://www.wunderground.com/weather/api

Other required items will be the packages for the script to run on the Onion Omega 2. Copy and paste the following lines into your terminal in order to install the packages.
opkg update
opkg install python3 python-light python-urllib3 pyOledExp pyOmegaExpansion oled-exp
