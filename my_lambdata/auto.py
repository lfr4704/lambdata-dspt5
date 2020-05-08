# autos.py

class Auto():
    def __init__(self, make, model, year, color, num_wheels):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.num_wheels = num_wheels

    def drive(self):
        print("WE ARE DRIVING", self.model)

if __name__ == "__main__":
    car = Auto("Toyota", "Prius", 2020, "Blue", 4)
    print(car.make, car.model)
    car.drive()
    car2 = Auto("Tesla", "Model S", 2020, "Blue", 4)
    car2.drive()
    truck = Auto("Ford", "F150", 2020, "Blue", 4)
    truck.drive()
    truck2 = Auto("Tesla", "Cybertuck", 2020, "Blue", 4)
    truck2.drive()
