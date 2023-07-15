import self as self


class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This car is driving")

    def stop(self):
        print("This car is stopped")


car_1 = Car("Chevy", "Corvette", "2021", "Blue")
car_2 = Car("Ford", "Mustang", "2022", "Red")

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_2.drive()
car_2.stop()


