#!/usr/bin/env python

# Set up the different libraries used in the script.
import urllib2
import json

# Pull the data from Weather Underground.
# You need your own API Key (http://www.wunderground.com/weather/api)
# Choose a PWS (Personal Weather Station) close to your location.
APIKey = "<your api key>"
PWSID = "<your PWS ID>"
weatherdata = urllib2.urlopen("http://api.wunderground.com/api/"+APIKey+"/conditions/q/pws:"+PWSID+".json")
astrodata = urllib2.urlopen("http://api.wunderground.com/api/"+APIKey+"/astronomy/q/pws:"+PWSID+".json")
alertdata = urllib2.urlopen("http://api.wunderground.com/api/"+APIKey+"/alerts/q/pws:"+PWSID+".json")

weatherinfo = json.loads(weatherdata.read())
astroinfo = json.loads(astrodata.read())
alertinfo = json.loads(alertdata.read())

# Here we put all the data into their own variable to make it readable
# and easier to format in the web page.
loc = weatherinfo['current_observation']['observation_location']['full']
updt = weatherinfo['current_observation']['observation_time']
cond = weatherinfo['current_observation']['weather']
temps = weatherinfo['current_observation']['temperature_string']
feels = weatherinfo['current_observation']['feelslike_string']
windchill = weatherinfo['current_observation']['windchill_string']
heat = weatherinfo['current_observation']['heat_index_string']
dew = weatherinfo['current_observation']['dewpoint_string']
humidity = weatherinfo['current_observation']['relative_humidity']
pressure = weatherinfo['current_observation']['pressure_in']
# Check the value of the Pressure Trend and give it an understandable value instead.
if weatherinfo['current_observation']['pressure_trend'] == '+':
	trendinfo = 'upwards'
elif weatherinfo['current_observation']['pressure_trend'] == '-':
	trendinfo = 'downwards'
elif weatherinfo['current_observation']['pressure_trend'] == '0':
	trendinfo = 'constant'
elif weatherinfo['current_observation']['pressure_trend'] == '':
	trendinfo = 'N/C'
rain = weatherinfo['current_observation']['precip_today_string']
wind = weatherinfo['current_observation']['wind_string']
vis = weatherinfo['current_observation']['visibility_mi'] + " miles."
sunrise = astroinfo['sun_phase']['sunrise']['hour'] + ":" + astroinfo['sun_phase']['sunrise']['minute']
sunset = astroinfo['sun_phase']['sunset']['hour'] + ":" + astroinfo['sun_phase']['sunset']['minute']
moonrise = astroinfo['moon_phase']['moonrise']['hour'] + ":" + astroinfo['moon_phase']['moonrise']['minute']
moonset = astroinfo['moon_phase']['moonset']['hour'] + ":" + astroinfo['moon_phase']['moonset']['minute']
phase = astroinfo['moon_phase']['phaseofMoon']
illum = astroinfo['moon_phase']['percentIlluminated'] + " %"
# Check for an alert.  Display the appropriate values.
if 'type' in alertinfo:
	alert = alertinfo['alerts']['description']
	expir = alertinfo['alerts']['expires']
else:
	alert = "No weather alerts or special notices for this region at this time."
	expir = ""

# Here we grab the image urls to display in the page.
weaticon = weatherinfo['current_observation']['icon_url']
wstation = weatherinfo['current_observation']['history_url']
wunderground = weatherinfo['current_observation']['image']['url']

# Write the web page.  PHP isnt really needed, I just kicked it off that way for future growth.
# Make sure the path matches where you want the file to be displayed from.
f = open('/www/weather/index.php', 'w')
f.write('<?php\n')
f.write('\n')
f.write('?>\n')
f.write('<html>\n')
f.write('<head>\n')
f.write('<title>RD: Weather: '+updt+'</title>\n')
f.write('</head>\n')
f.write('<body bgcolor=efefef alink=yellow vlink=yellow link=yellow>\n')
f.write('<center>\n')
f.write('<table border=1>\n')
f.write('<tr bgcolor=363663><td colspan=2 align=center><font color=e6e6ff><b>Current Weather at my house: <a href='+wstation+'>'+loc+'</a></b></font></td></tr>\n')
f.write('<tr bgcolor=363663><td colspan=2 align=center><font color=e6e6ff><b>'+updt+'</b></font></td></tr>\n')
f.write('<tr bgcolor=efefef><td width=30%><b>Conditions</b></td><td align=center><img src='+weaticon+'><br>'+cond+'</td></tr>\n')
f.write('<tr bgcolor=efefef><td width=30%><b>Temperature</b></td><td> '+temps+'</td></tr>\n')
f.write('<tr bgcolor=efefef><td width=30%><b>Feels Like</b></td><td> '+feels+'</td></tr>\n')
f.write('<tr bgcolor=efefef><td width=30%><b>Windchill</b></td><td> '+windchill+'</td></tr>\n')
f.write('<tr bgcolor=efefef><td width=30%><b>Heat Index</b></td><td> '+heat+'</td></tr>\n')
f.write('<tr bgcolor=efefef><td width=30%><b>Dewpoint</b></td><td> '+dew+'</td></tr>\n')
f.write('<tr bgcolor=efefef><td width=30%><b>Relative Humidity</b></td><td> '+humidity+'</td></tr>\n')
f.write('<tr bgcolor=efefef><td width=30%><b>Pressure</b></td><td> '+pressure+' and trending '+trendinfo+'</td></tr>\n')
f.write('<tr bgcolor=efefef><td width=30%><b>Rainfall</b></td><td> '+rain+'</td></tr>\n')
f.write('<tr bgcolor=efefef><td width=30%><b>Wind</b></td><td> '+wind+'</td></tr>\n')
f.write('<tr bgcolor=efefef><td width=30%><b>Visibility</b></td><td> '+vis+'</td></tr>\n')
f.write('<tr bgcolor=363663><td colspan=2 align=center><font color=e6e6ff><b>Sun/Moon Information</b></font></td></tr>\n')
f.write('<tr bgcolor=efefef><td width=30%><b>Sun Rise</b></td><td> '+sunrise+'</td></tr>\n')
f.write('<tr bgcolor=efefef><td width=30%><b>Sun Set</b></td><td> '+sunset+'</td></tr>\n')
f.write('<tr bgcolor=efefef><td width=30%><b>Moon Rise</b></td><td>' +moonrise+'</td></tr>\n')
f.write('<tr bgcolor=efefef><td width=30%><b>Moon Set</b></td><td> '+moonset+'</td></tr>\n')
f.write('<tr bgcolor=efefef><td width=30%><b>Moon Phase</b></td><td> '+phase+'</td></tr>\n')
f.write('<tr bgcolor=efefef><td width=30%><b>Illuminiation</b></td><td> '+illum+'</td></tr>\n')
f.write('<tr bgcolor=363663><td colspan=2 align=center><font color=e6e6ff><b>Warnings?</b></font></td></tr>\n')
f.write('<tr bgcolor=efefef><td colspan=2>'+alert+'<p>'+expir+'</td></tr>\n')
f.write('</table>\n')
f.write('<p>\n')
f.write('Weather information brought to you by:<p>\n')
f.write('<a href=https://www.wunderground.com/?apiref=195759c3816c5574><img src='+wunderground+'></a>\n')
f.write('</center>\n')
f.write('</body>\n')
f.write('</html>\n')
f.close()

exit()
