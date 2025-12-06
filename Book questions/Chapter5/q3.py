class Vehicle:
    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving")

class Bike(Vehicle):
    def move(self):
        print("Bike is cycling")

vehicles = [Vehicle(), Car(), Bike()]
for vehicle in vehicles:
    vehicle.move()