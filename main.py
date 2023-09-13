import requests
import json
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
city = input("Enter your city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=969d99c6a8c041399e0131648231309&q={city}"
r = requests.get(url)
wd = json.loads(r.text)
temp = (wd["current"]["temp_c"])
tempfl = (wd["current"]["feelslike_c"])
humidity = (wd["current"]["humidity"])
wind_speed = (wd["current"]["wind_kph"])


s = (f"The current temperature in {city} is {temp} degree celcius and it feels like {tempfl}. The humidity index is {humidity} and winds are flowing with speed of {wind_speed} kilometer per hour")
speaker.Speak(s)
