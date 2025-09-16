#Kirjoita ohjelma, joka kysyy käyttäjältä lentoaseman ICAO-koodin.
# Ohjelma hakee ja tulostaa koodia vastaavan lentokentän nimen
# ja sen sijaintikunnan kurssilla käytettävästä lentokenttätietokannasta. ICAO-koodi on tallennettuna airport-taulun ident-sarakkeeseen.

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

#cursor.execute("SELECT name, municipality FROM airport")

#result = cursor.fetchone()


def find_airport_with_ICAO(koodi):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{koodi}'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return(result)


#(find_airport_with_ICAO("00CA"))

ICAO = input("kerro lentokentän ICAO koodi: ")
kenttä = (find_airport_with_ICAO(ICAO))
if kenttä == None:
    print("kenttää ei löydy antamallasi koodilla")
else:
    print(kenttä)

print("kiitos hakemisesta")



