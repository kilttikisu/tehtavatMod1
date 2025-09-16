#Kirjoita ohjelma, joka kysyy käyttäjältä kahden lentokentän ICAO-koodit.
# Ohjelma ilmoittaa lentokenttien välisen etäisyyden kilometreinä.
# Laskenta perustuu tietokannasta haettuihin koordinaatteihin.

# Laske etäisyys geopy-kirjaston avulla: https://geopy.readthedocs.io/en/stable/.
# Asenna kirjasto valitsemalla View / Tool Windows / Python Packages.
# Kirjoita hakukenttään geopy ja vie asennus loppuun.

import geopy

import mysql.connector

yhteys = mysql.connector.connect(
    port=3306,
    host="localhost",
    database="flight_game",
    user="root",
    password="Vale12!",
    autocommit=True
    )


#Leveyspiiri (latitude): Mittaa etäisyyttä päiväntasaajalta pohjoiseen tai etelään.
#Pituusaste (longitude):



from geopy import distance

coord1 = (60.32135905, 24.9472068000384)
coord2 = (22.308046, 113.918480)
etäisyys = distance.distance(coord1, coord2)

print(f" etäisyys lentokenttien välillä on: {etäisyys.km} -Kilometriä")


