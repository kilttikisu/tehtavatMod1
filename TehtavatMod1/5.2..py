# lukujen kysyjä
# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän
# merkkijonon lopetusmerkiksi. Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta
# suuruusjärjestyksessä
# suurimmasta alkaen. Vihje:
# listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi
# reverse=True.

#luvut = []


#while True:
  #  command = int(input("kerro luku:"))
  #  luvut.append(command)
  #  if command == "":
   #     break
#luvut.sort(reverse=true)



luvut = []

syöte = input("Anna luku ( tyhjä lopettaa): ")

while syöte != "":
    luvut.append(int(syöte))
    syöte = input("Anna luku ( tyhjä lopettaa): ")

luvut.sort(reverse=True)
print(luvut)

viisi_suurinta = luvut[:5]


