# tuuma senteiksi

tuuma = float(input("kerro lukumäärä tuumina:"))
senttimetri = tuuma * 2.54
while tuuma >= 0:
    print(f"luku senttimetreinä on {senttimetri}")
    break
if tuuma < 0:
    tuuma = False
    print("käytä positiivisia lukuja")
else:
    print("kiitos!")