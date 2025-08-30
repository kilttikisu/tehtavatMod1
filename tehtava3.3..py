# Hemoglobiini testeri
#Naisen normaali hemoglobiiniarvo on välillä 117-175 g/l.
#Miehen normaali hemoglobiiniarvo on välillä 134-195 g/l.
sukupuoli = input("Kerro Sukupuolesi ( mies/nainen):")

if sukupuoli == "nainen":
    hemoglobiini = int(input("kerro hemoglobiini arvosi (g/l):"))
    if hemoglobiini < 117:
        print("Hemoglobiinisi on alhainen")
    elif hemoglobiini > 175:
        print("Hemoglobiinisi on liian korkea")
    else:
        print ("hemoglobiinisi on sopivalla tasolla")
elif sukupuoli == "mies":
    hemoglobiini = int(input("kerro hemoglobiini arvosi (g/l):"))
    if hemoglobiini < 134:
        print("Hemoglobiinisi on alhainen")
    elif hemoglobiini > 195:
        print("Hemoglobiinisi on liian korkea")
    else : print("hemoglobiini on sopivalla tasolla.")

else:
    print("käytä oikeaa sukupuoli valintaa (mies/nainen)")







