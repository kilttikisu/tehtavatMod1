import mysql.connector

#importataan tietokanta yhteys ajuri
#otetaan tietokantayhteys -> "yhteys" muuttujaan sidotaan yhteys, muuttuja voi olla
# minkä niminen vain, muuttujalla vaan sidotaan yhteys, muuten muodostat yhteyden
# ja jos sitä ei sido mihinkään muuttujaan niin yhteys katoaa ku ohjelman sulkee.

yhteys = mysql.connector.connect(
    port=3306,
    host="localhost",
    database="flight_game",
    user="root",   # jos ei käytä rootti tiliä niin user=xxx ja salasana mitä määrittänykään
    password="Vale12!",
    autocommit=True
    )
#print(yhteys) voi printata näkyviin mihin muodostanu yhteyden

#luodaan osoitin ja sijoitetaan viittaus siihen muuttujaan
cursor = yhteys.cursor()
#käytetään osoitinta ( englanniks "cursor") tietokantahakuun
cursor.execute("SELECT name, iso_country FROM country")
#sql-commennot kirjotetaan samalla tavalla (isot kirjaimet) kuin sql-palveluun, auttaa
#koodin lukemisessa, tunnistaa heti mitkä on ollut sql komentoja
#print(cursor) näkee missä kohdassa cursori on tietokannassa.

#haetaan rivi kerrallaan tietoa " fetch-one"
result = cursor.fetchone(),
print(result)
result = cursor.fetchone()
print(result)

#haetaan useampi rivi kerrallaan "fetch-many", suluissa (3) ilmotetaan monta riviä

result = cursor.fetchmany(3)
print(result)
#HUOM. cursori jää aina siihen kohtaan mihin edellinen haku jäänyt ja jatkaa siitä.

#yleisin tapa " fetch-all": haetaan kaikki ( loput-jos cursori ei listan alussa) tulokset
result = cursor.fetchall()
print(result)

# tietoja saa listana,monikossa tai sanakirjassa, riippuu miten haet tietoa ajurilla.
# haettuja tietoja voi sitten jatkokäsitellä pythonilla
#samalla tavalla kuin muitakin listoja.

#tulostetaan tulosjoukko halutussa muodossa esim:
for country in result:
    print(f"maan {country[0]} maakoodi on: {country[1]}")


# ohjelma, joka hakee maan sen koodin perusteella

def get_country_name_by_code(code):
    sql = f"SELECT name FROM country WHERE iso_country = '{code}'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    result = cursor.fetchone()
    return result
#print(get_country_name_by_code("fi"))

# tehää käyttöliittymä maahakusovellukselle
country_code = input("Anna maakoodi:")
print(get_country_name_by_code(country_code))
print(f"maakoodi: {country_code}, hakutulos: {country}")

def add_country(code, name):
    sql = f"INSERT INTO country (iso_country, name) VALUES ('{code}', '{name}')"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    print(cursor)

#add_country('MYS', 'Myass')
#huom. jos saman maan ajaa sisää kaks kertaa niin saat error, koska maa jo lisätty.


