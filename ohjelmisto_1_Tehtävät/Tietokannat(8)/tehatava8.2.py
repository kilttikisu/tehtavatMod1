#Kirjoita ohjelma, joka kysyy käyttäjältä maakoodin (esimerkiksi FI)
# ja tulostaa kyseisessä maassa olevien lentokenttien lukumäärät tyypeittäin.
# Esimerkiksi Suomen osalta tuloksena on saatava tieto siitä, että pieniä lentokenttiä on 65 kappaletta, helikopterikenttiä on 15 kappaletta jne.

import mysql.connector

yhteys = mysql.connector.connect(
    port=3306,
    host="localhost",
    database="flight_game",
    user="root",
    password="Vale12!",
    autocommit=True
    )

#cursor = yhteys.cursor()


#result = cursor.fetchall()

def airport_types_by_country(maakoodi):
    sql = f"SELECT type,count(*) AS lukumäärä FROM airport WHERE iso_country = '{maakoodi}' GROUP BY TYPE;"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

#print(airport_types_by_country("FI"))

maakoodi = input("kerro maakoodi ja hae maan lentokentät:")
result = airport_types_by_country(maakoodi)
if not result:
    print("ei löydy maata antamallasi maakoodilla")
else:
    print(f"Maassa {maakoodi}, on seuraavat kentät: {result}")

print("kiitos hakemisesta")
