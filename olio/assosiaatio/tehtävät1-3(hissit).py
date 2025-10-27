'''Kirjoita Hissi-luokka, joka saa alustajaparametreinaan alimman ja
ylimmän
 kerroksen numeron. Hissillä on metodit siirry_kerrokseen, kerros_ylös ja kerros_alas.
  Uusi hissi on aina alimmassa kerroksessa. Jos tee luodulle hissille h esimerkiksi metodikutsun h.siirry_kerrokseen(5), metodi kutsuu joko kerros_ylös- tai kerros_alas-metodia niin monta kertaa, että hissi päätyy viidenteen kerrokseen. Viimeksi mainitut metodit ajavat hissiä yhden kerroksen ylös- tai alaspäin ja ilmoittavat, missä kerroksessa hissi sen jälkeen on. Testaa luokkaa siten, että teet pääohjelmassa hissin ja käsket sen siirtymään haluamaasi kerrokseen ja sen jälkeen takaisin alimpaan kerrokseen.'''

'''
Jatka edellisen tehtävän ohjelmaa siten, että teet Talo-luokan. Talon alustajaparametreina annetaan alimman ja ylimmän kerroksen numero sekä hissien lukumäärä. Talon luonnin yhteydessä talo luo tarvittavan määrän hissejä. Hissien lista tallennetaan talon ominaisuutena. Kirjoita taloon metodi aja_hissiä, joka saa parametreinaan hissin numeron ja kohdekerroksen. Kirjoita pääohjelmaan lauseet talon luomiseksi ja talon hisseillä ajelemiseksi.


'''

class Hissi:
    def __init__(self,alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.kerros_nyt = alin_kerros


    def hissi_ylös(self,kertaa):
        if self.kerros_nyt < self.ylin_kerros:
            for k in range(kertaa):
                self.kerros_nyt = self.kerros_nyt + 1
        else:
            print("hissi on ylimässä kerroksessa")
        print(f"hissi on kerroksessa: {self.kerros_nyt}")

    def hissi_alas(self,kertaa):
        if self.kerros_nyt > self.alin_kerros:
            for k in range(kertaa):
                self.kerros_nyt = self.kerros_nyt - 1
        else:
            print("olet saavuttanut alimman kerroksen")
        print(f"hissi on kerroksessa: {self.kerros_nyt}")

    def siirry_kerrokseen(self,kerroksen_numero):
        if kerroksen_numero > self.ylin_kerros:
            print(f"suurin kerros on {self.ylin_kerros}")
        elif kerroksen_numero < self.alin_kerros:
            print(f"alin kerros on: {self.alin_kerros}")
        elif kerroksen_numero > self.kerros_nyt:
            kerroksia_ylös = kerroksen_numero - self.kerros_nyt
            self.hissi_ylös(kerroksia_ylös)
        elif kerroksen_numero < self.kerros_nyt:
            kerroksia_alas = self.kerros_nyt - kerroksen_numero
            self.hissi_alas(kerroksia_alas)
        else:
            print("kerrosta ei löydy")

class Talo:
   def __init__(self,h_kpl, k_alin, k_ylin):
       self.k_alin = k_alin
       self.k_ylin = k_ylin
       self.h_kpl = h_kpl
       self.hissit = []
       for i in range(h_kpl):
            hissi = Hissi(k_alin,k_ylin)
            self.hissit.append(hissi)

    def aja_hissiä(self,h_numero,t_kerros):



talo1 = Talo(2, 0, 5)

print(talo1.hissit[0].kerros_nyt)
