# funktio esimerkkejä

#def = defy, eli määritä funktio

#Funktio joka ei ota parametrejä, eikä palauta mitään.
def say_hello():
    print("hellou")
    print("you")
#say_hello()

# print (say_hello) -> käsky: #say_hello()
#print(say_hello()) suorittaa funktion ja tulostaa paluuarvon(return) "none" koska ei ole
#mitään parametrejä itse funktiossa, pelkästään tulostus pyyntö


def say_hello_v2(username, age):
    print("hellou")
    print(username)
    print(f"ikäsi: {age}")

#say_hello_v2("vallu",28)

# tässä funktiossa on nyt kaksi inputtia eli parametriä ja antaa takas kaks outputtia
#eli returnia.
'''

def say_hello_v2(username, age):
    print("hellou")
    print(username)
    print(f"ikäsi: {age}")
    return f"hello{username}!, age{age}"
'''
#return käsky funktiossa-> on sama ku loopeissa "break" eli lopettaa koodin ajon funktiossa.
#voidaan myös määritellä paluuarvo eli return funktiolle, kirjottamalla mitä palautetaan
# funktion ajon lopussa, returnin jälkeen.

#yllämainittu funktio toimii myös näin siis:
def say_hello_v2(username, age):
    return f"hello{username}!, age{age}"

print(say_hello_v2("vallu",5))

#Funktion idea koodata joku toiminto jota käyttää useein,jotta ei tarviis koodata jokasta
#toimintoa erikseen

#Esim python sisäänkoodattu funktio sum() joka plussaa kaikki alkiot yhteen.

numbers = [1,2,3,4,5]
print(sum(numbers))

#jos tätä funktioo ei olis olemassa, niin sen voisi koodata itselleen:

def my_sum(numbers_list):
    total = 0
    for n in numbers_list:
        total = total + n
    return total

print(my_sum(numbers))

#toinen esim.
''' 
app_running = True
while app_running:
    command = input("komento> ")
    print(f"komentosi oli: {command}")
    if command == "exit":
        app_running = False
    elif command == "laskukone":
        luku1 = float(input("kerro ensimmäinen luku:"))
        luku2 = float(input("kerro toinen luku:"))
        tulos_yhteenlasku = luku1 + luku2
        print(f"tulos on:" + str(tulos_yhteenlasku))

#koodin loppuosan eli " laskukoneen" voi muuttaa omaksi funktioksi
'''

def calculator():

    luku1 = float(input("kerro ensimmäinen luku:"))
    luku2 = float(input("kerro toinen luku:"))
    tulos_yhteenlasku = luku1 + luku2
    print(f"tulos on:" + str(tulos_yhteenlasku))

#eli yllä oleva funktio niin pääsis käyttää vaa käskyllä: calculator()

#eli lyhenetty ja cleenimpi koodi kokonaan olis uudella funktiolla:

app_running = True
while app_running:
    command = input("komento> ")
    print(f"komentosi oli: {command}")
    if command == "exit":
        app_running = False
    elif command == "laskukone":
        calculator()



