# while lukukone
app_running = True
luvut = []

while app_running:
    command = input("Kerro luku: ")

    if command == "":
        app_running = False
        if luvut:
            print(f"Suurin lukusi oli {max(luvut)} ja pienin lukusi oli {min(luvut)}")
    else:
        luku = float(command)
        luvut.append(luku)
        print(f"Lukusi oli {luku}")