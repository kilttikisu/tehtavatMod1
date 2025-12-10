import json
import requests

city_name = input("anna kaupungin nimi:")

API_key = "17e9c9a43ff48a813bee0d105cf6f555"

lang = "fi"

pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=metric&lang={lang}"

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code==200:
        hakutulos = vastaus.json()
        print(f"paikan {city_name} aste tilanne on seuraava: {hakutulos["main"]["temp"]} (celsius)")
        print(f"paikan {city_name} säätila on tällä hetkellä:{hakutulos["weather"][0]["description"]}")
except requests.exceptions.RequestException as e:
    print ("Hakua ei voitu suorittaa.")