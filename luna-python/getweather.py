# import module
import requests
import bs4
def get_weather(city):
	# Generating the url
	url = "https://google.com/search?q=weather+in+" + city
	# Sending HTTP request
	request_result = requests.get( url )
	# Pulling HTTP data from internet
	return bs4.BeautifulSoup( request_result.text,"html.parser").find( "div" , class_='BNeawe' ).text
		

