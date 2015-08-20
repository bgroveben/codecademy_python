# -*- coding: utf-8 -*-
print
"""
Inheritance is a tricky concept, so let's go through it step by step.

Inheritance is the process by which one class takes on the attributes and methods of another, and it's used to express an is-a relationship. For example, a Panda is a bear, so a Panda class could inherit from a Bear class. However, a Toyota is not a Tractor, so it shouldn't inherit from the Tractor class (even if they have a lot of attributes and methods in common). Instead, both Toyota and Tractor could ultimately inherit from the same Vehicle class.
"""
# We've defined a class, Customer, as well as a ReturningCustomer class that inherits from Customer.
# Note that we don't define the display_cart method in the body of ReturningCustomer,
# but it will still have access to that method via inheritance.
class Customer(object):
    """Produces objects that represent customers."""
    def __init__(self, customer_id):
        self.customer_id = customer_id

    def display_cart(self):
        print "I'm a string that stands in for the contents of your shopping cart!"

class ReturningCustomer(Customer):
    """For customers of the repeat variety."""
    def display_order_history(self):
        print "I'm a string that stands in for your order history!"

monty_python = ReturningCustomer("ID: 12345")
monty_python.display_cart()
monty_python.display_order_history()
print


"""
In Python, inheritance works like this:

class DerivedClass(BaseClass):
    # code goes here
where DerivedClass is the new class you're making and BaseClass is the class from which that new class inherits.
"""
# Create your own class, Triangle, that inherits from Shape, like this:
# class Triangle(Shape):
    # code goes here
# Inside the Triangle class, write an __init__() function that takes four arguments: self, side1, side2, and side3.
# Inside the __init__() function, set self.side1 = side1, self.side2 = side2, and self.side3 = side3.
class Shape(object):
    """Makes shapes!"""
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides

# Add your Triangle class below!
class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

equilateral = Triangle(10, 10, 10)
print equilateral
print Triangle.__bases__
print


"""
Sometimes you'll want one class that inherits from another to not only take on the methods and attributes of its parent, but to override one or more of them.

class Employee(object):
    def __init__(self, name):
        self.name = name
    def greet(self, other):
        print "Hello, %s" % other.name

class CEO(Employee):
    def greet(self, other):
        print "Get back to work, %s!" % other.name

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!
Rather than have a separate greet_underling method for our CEO, we override (or re-create) the greet method on top of the base Employee.greet method. This way, we don't need to know what type of Employee we have before we greet another Employee.
"""
# Create a new class, PartTimeEmployee, that inherits from Employee.
# Give your derived class a calculate_wage method that overrides Employee's. It should take self and hours as arguments.
# Because PartTimeEmployee.calculate_wage overrides Employee.calculate_wage, it still needs to set self.hours = hours.
# It should return the part-time employee's number of hours worked multiplied by 12.00
# (that is, they get $12.00 per hour instead of $20.00).
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00


"""
On the flip side, sometimes you'll be working with a derived class (or subclass) and realize that you've overwritten a method or attribute defined in that class' base class (also called a parent or superclass) that you actually need. Have no fear! You can directly access the attributes or methods of a superclass with Python's built-in super call.

The syntax looks like this:

class Derived(Base):
   def m(self):
       return super(Derived, self).m()
Where m() is a method from the base class.
"""
# First, inside your PartTimeEmployee class:
# Add a new method called full_time_wage with the arguments self and hours.
# That method should return the result of a super call to the calculate_wage method of PartTimeEmployee's parent class.
# Use the example above for help.
# Then, after your class:
# Create an instance of the PartTimeEmployee class called milton. Don't forget to give it a name.
# Finally, print out the result of calling his full_time_wage method.
# You should see his wage printed out at $20.00 per hour! (That is, for 10 hours, the result should be 200.00.)
class Employee(object):
    """Models real-life employees!"""
    def __init__(self, employee_name):
        self.employee_name = employee_name

    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
    def calculate_wage(self, hours):
        self.hours = hours
        return hours * 12.00

    def full_time_wage(self, hours):
        return super(PartTimeEmployee, self).calculate_wage(hours)

milton = PartTimeEmployee("Milton")
print milton.full_time_wage(10)
print
