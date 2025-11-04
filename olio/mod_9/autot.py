class Car:
    def __init__(self):
        self.speed = 0
        self.trip = 0
        self.top_speed = 100
        self.register_number = "ABC-123"

    def accelerate(self):
        self.speed += 1


car1 = Car()
car1.accelerate()
car1.accelerate()
car1.accelerate()
car1.accelerate()
car1.accelerate()

car2 = Car()

''' voi myös luoda listan autoista ja viitata listan yksikköön:

cars = [car(), Car()] 

cars[0].accelerate()   = kiihdyttää listan ekaa autoa, eli ensimmäistä autoa.

TAI

luodaan for looppi joka luo esim. 9 autoa listaan:

cars = []
for i in range 9
    cars.append(Car())

kiihdytetään listan autoa numero 2 = cars[1].accelerate

ja sit voi luoda while loopin joka tulostaa koko listan autot ja niiden nopeudet.



print(f"Auton 1 nopeus: {car1.speed}, auton 2 nopeus : {car2.speed}")

'''