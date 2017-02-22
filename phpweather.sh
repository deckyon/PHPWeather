#!/bin/ash

# Remove the old weather file.
# Make sure you point this to wherever you have your webserver running from
rm /www/weather/index.php

# Run the python script to pull the weather and create the webpage.
python /smb/scripts/phpweather.py

exit 0
