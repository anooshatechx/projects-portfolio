# Bilingual Translation
import requests
import json
from urdu_roman.romanize import Romanizer
r = Romanize()
while True:
	user = input("Enter your sentence: ")
	link = "https://api.mymemory.translated.net/get"
	param = {"q":user,"langpair":"en|ur"}
	extract = requests.get(link,params = param)
	convert = extract.json()
	x = convert["matches"][0]["translation"]
	trans = input("Do you want Simple Urdu or Roman Urdu? (u/r): ")
	if trans.strip().lower() in ["urdu","u"]:
		print("Simple Urdu translation: ",x)
	else:
		rom = r.romanize(x)
		print("Roman Urdu translation: ",rom)
	again = input("Another translation? y/n: " )
	if again.strip().lower() not in ["y","yes"]:
		print("Goodbye! See ya again 💗")
		break
	else:
		print("Yayyy! Lets go 🎯")
