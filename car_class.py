# -*- coding: utf-8 -*-
print
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg

    def display_car(self):
        return "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg)

my_car = Car("DeLorean", "silver", 88)
print my_car.condition
print my_car.display_car()
print


"""
We can modify variables that belong to a class the same way that we initialize those member variables. This can be useful when we want to change the value a variable takes on based on something that happens inside of a class method.
"""
# Inside the Car class, add a method drive_car() that sets self.condition to the string "used".
# Remove the call to my_car.display_car() and instead print only the condition of your car.
# Then drive your car by calling the drive_car() method.
# Finally, print the condition of your car again to see how its value changes.
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg

    def display_car(self):
        return "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg)

    def drive_car(self):
        self.condition = "used"

my_car = Car("DeLorean", "silver", 88)
print my_car.condition
my_car.drive_car()
print my_car.condition
print


# Create a class ElectricCar that inherits from Car.
# Give the new class an __init__() method of that includes a "battery_type" member variable in addition to the model, color and mpg.
# Then, create an electric car named "my_car" with a "molten salt" battery_type.
# Supply values of your choice for the other three inputs (model, color and mpg).
class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type = battery_type

my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")


# Inside ElectricCar add a new method drive_car() that changes the car's condition to the string "like new".
# Then, outside of ElectricCar, print the condition of my_car
# Next, drive my_car by calling the drive_car() function
# Finally, print the condition of my_car again
class Car(object):
    condition = "new"
    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg   = mpg

    def display_car(self):
        return "This is a %s %s with %s MPG." % (self.color, self.model, self.mpg)

    def drive_car(self):
        self.condition = "used"

my_car = Car("DeLorean", "silver", 88)
print my_car.condition
my_car.drive_car()
print my_car.condition
print

class ElectricCar(Car):
    def __init__(self, model, color, mpg, battery_type):
        self.model = model
        self.color = color
        self.mpg = mpg
        self.battery_type = battery_type

    def drive_car(self):
        self.condition = "like new"

my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
my_car.drive_car()
print my_car.condition
print

