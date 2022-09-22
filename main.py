'''
Uses the AccuWeather API to retrieve information about weather.
Uses the Twitter API to post to twitter account

You will need to sign up for an AccuWeather account and Twitter Developer account
to customize this script for your own use
'''

#imports
import tweepy
import requests
import json
import os
from datetime import datetime
from geopy.geocoders import Nominatim
import pytz


#AccuWeather api set up
geolocator = Nominatim(user_agent="MyApp")
#can replace with other city. "City, state"
city_name = "Oceanside, CA"
location = geolocator.geocode(city_name)
latitude_city = location.latitude
longitude_city = location.longitude
units = 'imperial'
#print(latitude_city, longitude_city)
API_key = "replace with api key"
complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?lat={latitude_city}&lon={longitude_city}&units={units}&appid={API_key}"
response = requests.get(complete_api_link)
temp = response.json()['main']['temp']
feel_like_temp = response.json()['main']['feels_like']
description = response.json()['weather'][0]["description"]
date_time = datetime.now(pytz.timezone("America/Los_Angeles"))
#print(date_time)
months_in_year = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
post = f'The weather today at MiraCosta College is {temp} degrees'

#twitter api function
def post_tweet(data):
    client = tweepy.Client(consumer_key='replace with consumer key',
                           consumer_secret='replace with consumer secret',
                           access_token='replace with access token',
                           access_token_secret='replace with access token secret')

    # Replace the text with whatever you want to Tweet about
    response = client.create_tweet(text=data)

    print(response)

def main():
    post_tweet(post)

if __name__ == '__main__':
    main()