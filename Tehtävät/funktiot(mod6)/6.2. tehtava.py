#Muokkaa edellistä funktiota siten, että funktiot(mod6) saa parametrinaan
# nopan tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.
import random

def nopanheitto():
    tahkojen_lukumäärä = maksimiluku
    luku = random.randint(0, int(tahkojen_lukumäärä))
    print(f"tulos on : {luku}")
    while int(luku) < int(tahkojen_lukumäärä):
        True is True
        if int(luku) == int(tahkojen_lukumäärä):
            break

print("selvitä monta nopan heittoa kestää saada maksimiluku")
app_running = True
while app_running:
    maksimiluku = input(" kerro nopan suurin numeroarvo( käytä kokonaisia numeroita)")
    nopanheitto()
print("kiitos pelaamisesta")
