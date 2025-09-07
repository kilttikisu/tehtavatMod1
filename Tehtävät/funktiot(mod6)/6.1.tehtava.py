#Kirjoita parametriton funktiot(mod6), joka palauttaa paluuarvonaan satunnaisen <
# nopan silmäluvun väliltä 1..6.
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

import random

def nopanheitto():
    silmäluku = random.randint(1,6)
    print(f"tulos on : {silmäluku}")
    return silmäluku

#nopanheitto()

app_running = True
while app_running:
    silmäluku = nopanheitto()
    if silmäluku == 6:
        app_running = False




