import random
N = int(input("Anna arvottavien pisteiden määrä: "))

sisalla = 0

i = 0
while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 <= 1:
        sisalla += 1

    i += 1

pi_approx = 4 * sisalla / N
print(f"Arvio piille {N} pisteellä on {pi_approx}")