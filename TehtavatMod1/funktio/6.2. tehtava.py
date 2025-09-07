#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan
# nopan tahkojen yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa. Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.
import random



def nopanheitto():
    maksimiluku = input("kerro maksimiluku(käytä kokonaisia numeroita):")
    print(f"nopan maksimiluku {maksimiluku}")
    tahkojen_lukumäärä = int(maksimiluku)
    print(f"nopassa on {tahkojen_lukumäärä} tahkoa")
    luku = random.randint(0, int(maksimiluku))
    print(f"tulos on : {luku}")
    return luku

#print(input("kerro nopan maksimiluku"))
#nopanheitto()

'''
app_running = True
while app_running:
    nopanheitto()
    
    '''



#nopanheitto()
'''
app_running = True
while app_running:
    silmäluku = nopanheitto()
    if silmäluku == 6:
        app_running = False
        '''
