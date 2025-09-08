#Muokkaa edellistä funktiota siten, että funktiot(mod6) saa parametrinaan
# nopan tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.
import random

maksimiluku = input(" kerro nopan suurin numeroarvo( käytä kokonaisia numeroita)")

def nopanheitto_maksimilukuun(tahkojen_lukumäärä):
    maksimiluku = tahkojen_lukumäärä
    heitot = 0
    nopanheitto = random.randit(1, int(tahkojen_lukumäärä))
    nopanheitto = heitot + 1
    print(f" heiton tulos {nopanheitto}")
    while nopanheitto < tahkojen_lukumäärä:
        print(nopanheitto)

nopanheitto_maksimilukuun(tahkojen_lukumäärä)


print("selvitä monta nopan heittoa kestää saada maksimiluku")


print("kiitos pelaamisesta")
