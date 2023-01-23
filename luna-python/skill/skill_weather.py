

def skill_weather(*args):
	import core.luna_core as coremodules
	import core.luna_utils as lunautils
	import requests
	import bs4
	import geocoder
	import sys
	import core.luna_core as coremodules
	city = geocoder.ip('me').city
		# Generating the url
	url = "https://google.com/search?q=weather+in+" + city
		# Sending HTTP request
	request_result = requests.get( url )
		# Pulling HTTP data from internet
	coremodules.luna_speak( bs4.BeautifulSoup( request_result.text,"html.parser").find( "div" , class_='BNeawe' ).text)

skill_weather()		

