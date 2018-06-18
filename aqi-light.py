import requests
import json
import subprocess

def change_colour (hue, saturation):
	cmd = """curl -X PUT --header "Content-Type:Application/json" --header "authorization: 092-94-999" http://192.168.31.95:51826/characteristics --data '
{"characteristics":[{"aid":38,"iid":12,"value":""" + str(hue) + """},{"aid":38,"iid":13,"value":""" + str(saturation) + """ }]}'"""
	process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

def turn_on_light ():
	cmd = """curl -X PUT --header "Content-Type:Application/json" --header "authorization: 092-94-999" http://192.168.31.95:51826/characteristics --data '{"characteristics":[{"aid":38,"iid":10,"value":true,"status":0}]}'"""
	process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)	

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


