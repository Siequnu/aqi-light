# Script to turn on a Yeelight based on pollution data
# Uses YeeCli https://gitlab.com/stavros/yeecli/

import requests
import json
import os

def change_colour (hue, saturation):
	cmd = 'yee --ip=192.168.31.55 hsv ' + str(hue) + ' ' + str(saturation) 
	os.system (cmd)
def turn_on_light ():
	cmd = 'yee --ip=192.168.31.55 brightness 10'
	os.system('yee --ip=192.168.31.55 brightness 10')

api_token = '8a26809e31dc3953bacdff5795091a22f52960dd'
request = "http://api.waqi.info/search/?keyword=beijing&token=" + api_token

r = requests.get(request)
json_data = r.json()

beijing_us_embassy_aqi = None
for station in json_data['data']:
	if (station['station']['url']) == 'beijing/us-embassy':
		
		beijing_us_embassy_aqi = int(station['aqi'])

turn_on_light ()
if beijing_us_embassy_aqi != None:
	if beijing_us_embassy_aqi < 100:
		change_colour (132, 100) # Turn light green
	elif beijing_us_embassy_aqi < 150:
		change_colour (32, 100) # Orange
	elif beijing_us_embassy_aqi < 200:
		change_colour (353, 100) # Red
	else:
		change_colour (283, 100) # Purple


