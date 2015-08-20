# -*- coding: utf-8 -*-
print
# A class is just a way of organizing and producing objects with similar attributes and methods.
# We've defined our own class, Fruit, and created a lemon instance.
class Fruit(object):
    """A class that makes various tasty fruits."""
    def __init__(self, name, color, flavor, poisonous):
        self.name = name
        self.color = color
        self.flavor = flavor
        self.poisonous = poisonous

    def description(self):
        print "I'm a %s %s and I taste %s." % (self.color, self.name, self.flavor)

    def is_edible(self):
        if not self.poisonous:
            print "Yep! I'm edible."
        else:
            print "Don't eat me! I am super poisonous."

lemon = Fruit("lemon", "yellow", "sour", False)

lemon.description()
lemon.is_edible()
print


# A basic class consists only of the class keyword, the name of the class, and the class from which
# the new class inherits in parentheses.
# Create a class called Animal.
class Animal(object):
    # The __init__() function is required for classes, and it's used to initialize the objects it creates.
    # __init__() always takes at least one argument, self, that refers to the object being created.
    def __init__(self, name):
        self.name = name

    def announce(self):
        print "Hi, my name is %s." % (self.name)

zebra = Animal("Jeffrey")
print zebra.name
zebra.announce()
print


"""
As mentioned, you can think of __init__() as the method that "boots up" a class' instance object: the init bit is short for "initialize."

The first argument __init__() gets is used to refer to the instance object, and by convention, that argument is called self. If you add additional arguments—for instance, a name and age for your animal—setting each of those equal to self.name and self.age in the body of __init__() will make it so that when you create an instance object of your Animal class, you need to give each instance a name and an age, and those will be associated with the particular instance you create.
"""
# Class definition
class Animal(object):
    """Makes cute animals."""
    # For initializing our instance objects
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry  # A default boolean like 'True' would also work.
# Note that self is only used in the __init__()
# function definition; we don't need to pass it
# to our instance objects.

zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 1, False)
panda = Animal("Chad", 7, True)

print zebra.name, zebra.age, zebra.is_hungry
print giraffe.name, giraffe.age, giraffe.is_hungry
print panda.name, panda.age, panda.is_hungry
print


"""
Another important aspect of Python classes is scope. The scope of a variable is the context in which it's visible to the program.

It may surprise you to learn that not all variables are accessible to all parts of a Python program at all times. When dealing with classes, you can have variables that are available everywhere (global variables), variables that are only available to members of a certain class (member variables), and variables that are only available to particular instances of a class (instance variables).

The same goes for functions: some are available everywhere, some are only available to members of a certain class, and still others are only available to particular instance objects.
"""
# Note that each individual animal gets its own name and age (since they're all initialized individually),
# but they all have access to the member variable is_alive, since they're all members of the Animal class.
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age

zebra = Animal("Jeffrey", 2)
giraffe = Animal("Bruce", 1)
panda = Animal("Chad", 7)

print zebra.name, zebra.age, zebra.is_alive
print giraffe.name, giraffe.age, giraffe.is_alive
print panda.name, panda.age, panda.is_alive
print


# Add a method, description, to your Animal class.
# Using two separate print statements, it should print out the name and age of the animal it's called on.
# Then, create an instance of Animal, hippo (with whatever name and age you like), and call its description method.
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def description(animal):
        print animal.name
        print animal.age

hippo = Animal("Ben", 21)
hippo.description()
print


"""
A class can have any number of member variables. These are variables that are available to all members of a class.

hippo = Animal("Jake", 12)
cat = Animal("Boots", 3)
print hippo.is_alive
hippo.is_alive = False
print hippo.is_alive
print cat.is_alive

In the example above, we create two instances of an Animal.
Then we print out True, the default value stored in hippo's is_alive member variable.
Next, we set that to False and print it out to make sure.
Finally, we print out True, the value stored in cat's is_alive member variable. We only changed the variable in hippo, not in cat.
"""
# Let's add another member variable to Animal.
# After line 3, add a second member variable called health that contains the string "good".
# Then, create two new Animals: sloth and ocelot. (Give them whatever names and ages you like.)
# Finally, on three separate lines, print out the health of your hippo, sloth, and ocelot.
class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def description(animal):
        print animal.name
        print animal.age

hippo = Animal("Ben", 21)
hippo.description()
sloth = Animal("Simon", 18)
ocelot = Animal("Ollie", 32)
print hippo.health
print sloth.health
print ocelot.health
print


"""
Classes like Animal and Fruit make it easy to understand the concepts of classes and instances, but you probably won't see many zebras or lemons in real-world programs.

However, classes and objects are often used to model real-world objects. The code in the editor is a more realistic demonstration of the kind of classes and objects you might find in commercial software. Here we have a basic ShoppingCart class for creating shopping cart objects for website customers; though basic, it's similar to what you'd see in a real program.
"""
# Create an instance of ShoppingCart called my_cart.
# Initialize it with any values you like, then use the add_item method to add an item to your cart.
class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."

my_cart = ShoppingCart("Ben")
my_cart.add_item("toothpaste", 2)
print my_cart.items_in_cart
print
