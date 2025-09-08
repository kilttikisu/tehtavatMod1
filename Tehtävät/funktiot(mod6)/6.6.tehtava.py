#Kirjoita funktio, joka saa parametreinaan
# pyöreän pizzan halkaisijan senttimetreinä sekä pizzan hinnan euroina.
# Funktio laskee ja palauttaa pizzan yksikköhinnan euroina per neliömetri.
# Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat ja hinnat sekä ilmoittaa,
# kumpi pizza antaa paremman vastineen rahalle (eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä kirjoitettua funktiota.

import math

def pitsan_hinta_per_m2(halkaisija_cm, hinta_euro):
    halkaisija_m = halkaisija_cm / 100
    pinta_ala_m2 = math.pi * (halkaisija_m / 2) ** 2
    hinta_per_m2 = hinta_euro / pinta_ala_m2
    return hinta_per_m2

# Syötteet käyttäjältä
print("Syötä tiedot Pitsa 1:")
d1 = float(input("Halkaisija (cm): "))
h1 = float(input("Hinta (€): "))

print("\nSyötä tiedot Pitsa 2:")
d2 = float(input("Halkaisija (cm): "))
h2 = float(input("Hinta (€): "))

# Lasketaan hinnat per neliömetri
hinta1 = pitsan_hinta_per_m2(d1, h1)
hinta2 = pitsan_hinta_per_m2(d2, h2)

# Tulostus
print(f"\nPitsa 1: {hinta1:.2f} €/m²")
print(f"Pitsa 2: {hinta2:.2f} €/m²")

# Vertailu
if hinta1 < hinta2:
    print("➡️ Pitsa 1 on edullisempi neliöhinnaltaan.")
elif hinta2 < hinta1:
    print("➡️ Pitsa 2 on edullisempi neliöhinnaltaan.")
else:
    print("🤝 Molemmat pitsat ovat yhtä edullisia neliöhinnaltaan.")
