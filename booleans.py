"""
     Boolean Operators
------------------------
True and True is True
True and False is False
False and True is False
False and False is False

True or True is True
True or False is True
False or True is True
False or False is False

Not True is False
Not False is True

"""

bool_one = False and False

bool_two = -(-(-(-2))) == -2 and 4 >= 16**0.5

bool_three = 19 % 4 != 300 / 10 / 10 and False

bool_four = -(1**2) < 2**0 and 10 % 10 <= 20 - 10 * 2

bool_five = True and True

print bool_one
print bool_two
print bool_three
print bool_four
print bool_five
print


bool_one = 2**3 == 108 % 100 or 'Cleese' == 'King Arthur'

bool_two = True or False

bool_three = 100**0.5 >= 50 or False

bool_four = True or True

bool_five = 1**100 == 100**1 or 3 * 2 * 1 != 3 + 2 + 1

print bool_one
print bool_two
print bool_three
print bool_four
print bool_five
print


bool_one = not True

bool_two = not 3**4 < 4**3

bool_three = not 10 % 3 <= 10 % 2

bool_four = not 3**2 + 4**2 != 5**2

bool_five = not not False

print bool_one
print bool_two
print bool_three
print bool_four
print bool_five
print


bool_one = False or not True and True

bool_two = False and not True or True

bool_three = True and not (False or False)

bool_four = not not True or False and not True

bool_five = False or not (True and True)

print bool_one
print bool_two
print bool_three
print bool_four
print bool_five
print

# Use boolean expressions as appropriate on the lines below!

# Make me false!
bool_one = (2 <= 2) and "Alpha" == "Bravo"  # We did this one for you!

# Make me true!
bool_two = (1 != 2) or "one" == "two"

# Make me false!
bool_three = "one" == "two" and (1 != 2)

# Make me true!
bool_four = True and not False

# Make me true!
bool_five = (5 >= 3) and (1 < 10)

print bool_one
print bool_two
print bool_three
print bool_four
print bool_five
