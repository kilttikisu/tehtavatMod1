#Kirjoita funktio, joka saa parametrinaan bensiinin määrän
# Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän.
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi.
# Muunnos on tehtävä aliohjelmaa hyödyntäen. Muuntamista jatketaan siihen saakka,
# kunnes käyttäjä syöttää negatiivisen gallonamäärän. Yksi gallona on 3,785 litraa.

def litramuuntaja():
    gallon = float(input("kerro määrä yhdysvaltain galloina:"))
    litra = float((gallon)) * (3.785)
    print(f"määrä litroina {litra}")
    return litra

#litramuuntaja()

print("hei, tervetuloa käyttämään litramuuntajaa")
while float(litramuuntaja()) >= 0:
    True
else:
 print("käytä positiivia lukuja")

