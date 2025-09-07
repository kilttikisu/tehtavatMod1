# Kaupungin nimi lista

kaupungit = []

n = 5

for i in range(n):
    kaupunki = input(f"anna {i+1} kaupungin nimi :")
    kaupungit.append(kaupunki)

for k in kaupungit:
    print(k)