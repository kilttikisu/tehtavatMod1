#Kirjoita ohjelma lentoasematietojen hakemiseksi ja tallentamiseksi.
# Ohjelma kysyy käyttäjältä, haluaako tämä syöttää uuden lentoaseman,
# hakea jo syötetyn lentoaseman tiedot vai lopettaa. Jos käyttäjä valitsee uuden lentoaseman syöttämisen, ohjelma kysyy käyttäjältä lentoaseman ICAO-koodin ja nimen. Jos käyttäjä valitsee haun, ohjelma kysyy ICAO-koodin ja tulostaa sitä vastaavan lentoaseman nimen. Jos käyttäjä haluaa lopettaa, ohjelman suoritus päättyy. Käyttäjä saa valita uuden toiminnon miten monta kertaa tahansa aina siihen asti, kunnes hän haluaa lopettaa. (ICAO-koodi on lentoaseman yksilöivä tunniste. Esimerkiksi Helsinki-Vantaan lentoaseman ICAO-koodi on EFHK. Löydät koodeja helposti selaimen avulla.)

lentokenttädict = {
    "ARN": "ARLANDA",
    "EFHK": "Helsinki-Vantaa",
    "EETN": "Tallin",
}

#lentokonedict.update({"EVRA":"RIGA"})-> lisää lentokentän listaan
# haetaan sanakirjasta: listan nimi([mitä haetaan]) eli lentokenttädict([ARN]) esim.

ask = True

while ask:

    command = input("haluaako syöttää uuden lentoaseman (u), hakea jo syötetyn lentoaseman  tiedot(h) vai lopettaa (l).").lower()
    #lower() varmistaa että kaikki commandit tulee pienel kirjaimella, eli ihan sama laittaako
    # u vai U niin koodi toimii.

    if command == "u":
        print("lisätään uusi kenttä")
        ICAO = input("Anna ICAO-koodi").upper() #upper()-varmistaa et koodi tallentuu ISONA
        nimi = input("anna lentokentän nimi")
        lentokenttädict[ICAO] = nimi
        print("lentokenttä lisätty", lentokenttädict)
    elif command == "h":
        print("haetaan lentokenttä")
        lentokenttä = input("kerro lentokentän ICAO-koodi:").upper()
        if lentokenttä in lentokenttädict:
            print(f"haulla {lentokenttä} löytyi lentokenttä"), lentokenttädict([lentokenttä])
    elif command == "l":
        print("lopetetaan")
        ask = False
    else:
        print("virheellinen syöte")
        ask = False




