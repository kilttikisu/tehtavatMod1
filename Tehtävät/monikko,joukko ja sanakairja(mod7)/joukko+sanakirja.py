#joukko eli set {} on järjestämätön tietorakenne, eli sen alkiot voivat olla
# MISSÄ TAHANSA järjestyksessä!
#ALKIOIHIN EI VOI VIITATA INDEKSILLÄ
#TOISIN KUIN LISTASSA JA MONIKOSSA, alkio voi esiintyä joukossa  VAIN KERRAN!

#joukko annetaan aaltosulkeilla {}
# jos alkio toistuu,ei tuu virhettä, alkiota ei vaa oteta mukaan
joukko = {1,2,3,4,5,6,7}
print(joukko)
joukko2 = {1,2,3,4,5,6,6,6,6,6,6,7}
print(joukko2)

print("---------------------------------------------------")
# testataan monikon alkioiden tallentumista satunnaisessa järjestelmässä

pelit = {"Monopoli", "Shakki", "Cluedo", "uuno", "afrikantähti"}
print(pelit)

#alkioiden iteroiminen for/in toiminolla ok, mutta indeksiä ei voi käyttää kuten listassa.

for p in pelit:
    print(p)

if "uuno" in pelit:
    print("jes uuno löytyy")

print("-------------------------------------------------")

#tyhjän listan luominen

autolista = []
autolista.append("audi")
autolista.append("wolkkari")
print(autolista)

#tyhjän joukon luominen, pitää käyttää set-funktiota!

autojoukko = set()
autojoukko.add("audi")
autojoukko.add("mersu")
print(autojoukko)

print("-----------------------------------------")
# SANAKIRJA (dictionary)

#Sanakirjaan voidaan tallentaa avain-arvopareja. Avain on ikään kuin kahva,
# josta vetämällä oikea sanakirjan tietue löytyy, jotta sen arvon päästään käsiksi.

#sanakirjan alustaminen: annettaan avain-arvopari seuraavasti: AVAIN : ARVOPARI
# peräkkäiset avain-arvoparit erotellaan pilkulla.

oppilaat = { #voi myös asettaa arvot peräkkäin tähän, mut selkeempi kuten alla
    "matti": 25,
    "ossi": 26,
    "hermanni":50,
    "karvanenjalmari": 34,
}
print(oppilaat)

#mitkä on sanakirjan tietueet (itmes)
print(oppilaat.items())

#mitkä ovat avaimet sanakirjassa
print(oppilaat.keys())

#mitkä ovat arvot (values)
print(oppilaat.values())

# käydään sanakirja läpi for/in
for o in oppilaat:
    print(o)

avain = "matti"
oppilaat[avain]
print("etsitään avaimella matti hänen ikä", oppilaat[avain])
print(f" matin ikä on: {oppilaat["matti"]}")

# lisätään yhteystiedot sanakirjaan

yhteystiedot = {
    "matti": {"puh":"040456456"},
    "ossi": {"puh":"050556789"},
    "karvanenhalmari": {"puh":"044567890"}
}

print(f"matin puhelinnumero on: {yhteystiedot["matti"]["puh"]}")



