# Weather Data Fetcher
import requests
import json
while True:
	user = input("Enter a city name: ")
	link = ("https://api.openweathermap.org/data/2.5/weather")
	params = {"q" : user, "appid" : "YOUR_API_KEY_HERE", "units":"metric"}
	x = requests.get(link,params=params)
	y = x.json()
	if x.status_code != 200:
		print("City not found. Please try again")
		continue
	z = y["main"]["temp"]
	des = y["weather"][0]["description"]
	print(f"Weather in {user}: {z}°C, {des}")
	repeat = input("Wanna try another city? y/n: ")
	if repeat.strip().lower() not in ["y","yes"]:
		break
