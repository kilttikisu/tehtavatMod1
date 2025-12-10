class Car:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.speed = 0
        self.trip = 0
        self.top_speed = huippunopeus
        self.register_number = rekisteritunnus

    def accelerate(self, speed_change):
            self.speed += speed_change
            if self.speed > self.top_speed:
                self.speed = self.top_speed
            if self.speed < 0:
                self.speed = 0



car1 = Car("ABC-123",142)
print(car1.speed)
print(car1.trip)
print(car1.top_speed)
print(car1.register_number)
car1.accelerate(30)
car1.accelerate(70)
car1.accelerate(50)
print(car1.speed)
car1.accelerate(-200)
print(car1.speed)
