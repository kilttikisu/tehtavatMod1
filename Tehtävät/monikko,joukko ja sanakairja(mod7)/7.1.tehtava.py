#Kirjoita ohjelma, joka kysyy käyttäjältä kuukauden numeron, jonka jälkeen ohjelma
# tulostaa sitä vastaavan vuodenajan (kevät, kesä, syksy, talvi). Tallenna ohjelmassasi kuukausia vastaavat vuodenajat merkkijonoina monikkotietorakenteeseen. Määritellään kukin vuodenaika kolmen kuukauden mittaiseksi siten, että joulukuu on ensimmäinen talvikuukausi.

vuodenajat = (
    "talvi",
    "talvi",
    "kevät",
    "kevät",
    "kevät",
    "kesä",
    "kesä",
    "kesä",
    "syksy",
    "syksy",
    "syksy",
    "talvi",
)

kuukauden_numero = int(input("anna kuukauden numero(0-12):"))

if 1 <= kuukauden_numero <= 12:
    print(vuodenajat[kuukauden_numero-1])
else:
    print("väärä numero")