#Muokkaa edellistä funktiota siten, että funktiot(mod6) saa parametrinaan
# nopan tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.
import random

# Funktio, joka heittää noppaa, kunnes saadaan maksimi
def nopanheitto_maksimiin(tahkojen_lkm):
    heitot = 0
    while True:
        heitot += 1
        silmäluku = random.randint(1, tahkojen_lkm)
        print(f"Heitto {heitot}: {silmäluku}")
        if silmäluku == tahkojen_lkm:
            break
    return heitot

# Kysy käyttäjältä tahkojen lukumäärä
tahkot = int(input("Montako tahkoa nopassa on? "))

# Kutsu funktiota ja anna käyttäjän syöttämä luku parametrina
heittojen_maara = nopanheitto_maksimiin(tahkot)

# Tulosta tulos
print(f"\nSaatiin maksimiluku {tahkot} {heittojen_maara} heitolla.")
print("Kiitos pelaamisesta!")
