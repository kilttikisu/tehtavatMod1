#Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota ja tulostat sen palauttaman summan.

number_list = [1,2,3,4,6,7,9]


def sumlist(numbers_list):
    total = 0
    for n in numbers_list:
        total = total + n
    return total

print(sumlist(number_list))