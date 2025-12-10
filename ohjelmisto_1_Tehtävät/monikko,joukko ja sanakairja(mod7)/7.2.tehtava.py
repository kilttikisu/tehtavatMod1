#Kirjoita ohjelma, joka kysyy käyttäjältä nimiä siihen saakka,
# kunnes käyttäjä syöttää tyhjän merkkijonon. Kunkin nimen syöttämisen jälkeen ohjelma tulostaa joko tekstin Uusi nimi tai Aiemmin syötetty nimi sen mukaan, syötettiinkö nimi ensimmäistä kertaa. Lopuksi ohjelma luettelee syötetyt nimet yksi kerrallaan allekkain mielivaltaisessa järjestyksessä. Käytä joukkotietorakennetta nimien tallentamiseen.

# jos tekee vaan "nimilista" = {} -> niin tämä tulkitaan sanakirjaksi!
#siksi tyhjä joukko-lista, tehdään-> set()

nimijoukko = set()

while True:
    nimi = input("kerro nimi listaan:")
    if nimi == "": break
    if nimi in nimijoukko:
        print("nimi löytyy jo listasta")
    else:
        nimijoukko.add(nimi)
        print(f"nimi {nimi} lisätty listaan")

for n in nimijoukko:
    print(n)


