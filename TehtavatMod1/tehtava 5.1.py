# Arpakuutio summa

import random

n = int(input("Anna arpakuutioiden määrä"))

#heitot = []
total = 0

for i in range(n):
    heitto = random.randint(1, 6)
    print(heitto)
    total += heitto

print(f"arpakuutioiden yhteistulos on {total}")


print("----------------------------------------------------------------")



import random

n = int(input("Anna arpakuutioiden määrä"))

heitot = []


for i in range(n):
    heitto = random.randint(1, 6)
    print(heitto)
    heitot.append(heitto)

print(heitot)
print(sum(heitot))