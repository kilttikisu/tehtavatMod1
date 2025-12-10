#monikko
#monikko eli (tuple) on "kuin lista jota ei voi muokata"

lista = [1,2,3,4,5,6,]
print(lista)

monikko = (1,2,3,4,5,6)
monikko2 = 1,2,3,4,5,6,7 # monikon voi myös luoda ilman kaarisulkeita, mutta ei ole tapana.
print(monikko)
print(monikko2)

#monikko voi sisältää erillaista tietoa
monikko3 = (1, 2, "petteri", 4)
print(monikko3)

#luodun listan ja monikon eka alkio

print(lista[0])
print(monikko[0])

#toisin kuin lista, monikkoa ei voi muuttaa tai alkioita lisätä/poistaa yms.

lista[0] = 0
lista.append(7)
print("Muokattu lista on:",lista)

# monikko[0] = 0  antaa virheviestin " dubles(monikko) ei tue toimintoa"

luku = monikko[3] # monikosta voi hakea alkiota samanalailla kuin listastakin
print(luku)


print(" --------------------------------------------------------")
#monikon läpikäynti kuten listan

for i in monikko3:
    print(i)
''' 
for i in monikko3:
    print(i)
    if i == "petteri":
        print("sana löytyi")
        '''
#sama kuin ylempi käytettynä in-hakua.
if "petteri" in monikko3:
    print("petteri löyty")
print("--------------")

#monikon arvojen purku muuttujiin
hedelmät = ("persikka", "mandariini","omena")
(eka,toka,kolmas) = ("persikka","mandariini","omena")
(eka,toka,kolmas) = hedelmät

print( "eka hedelmä on", eka)
print("viimenen hedelmä on", kolmas)

#hedelmä funktio, monikon voi antaa funktion parametrinä

def tulosta_monikko(hedelmät):
    for h in hedelmät:
        print(h)
tulosta_monikko(hedelmät)

#monikko funktio paluuarvona
import random

def noppa_heitto():
    noppa1 = random.randint(1,6)
    noppa2 = random.randint(1,6)
    print(f"nopista tuli luvut {noppa1} ja {noppa2}")

noppa_heitto()

# sama random funktio yksinkertaistettuna

def noppa_heitto2():
    eka, toka = random.randint(1,6), random.randint(1,6)
    print(f"ekasta tuli {eka} ja tokasta {toka}")
noppa_heitto2()

# palautetaan arvo funktiossa

def noppa_heitto3():
    eka, toka = random.randint(1,6), random.randint(1,6)
    print(f"ekasta tuli {eka} ja tokasta {toka}")
    return eka, toka
noppa_heitto3()

