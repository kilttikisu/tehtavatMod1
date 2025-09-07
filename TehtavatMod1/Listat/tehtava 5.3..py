# alkuluku vai ei

luku = int(input("anna luku ja tarkistetaan onko se alkuluku:"))
jaollinen = []

#oletusarvo on että luku on alkuluku, todennettaan jakamalla
onko_alkuluku = True

#tehää looppi ja jaetaan syötetty numero kaikilla numeroilla välillä 2-100

for i in range(2,luku):
    print(i)
    if luku % i == 0:
        onko_alkuluku = False
        jaollinen.append(i)
if onko_alkuluku:
    print(f"{luku} on alkuluku")
else:
    print(f"{luku} ei ole alkuluku")

print(jaollinen)

