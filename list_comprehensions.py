# -*- coding: utf-8 -*-

"""
Let's say you wanted to build a list of the numbers from 0 to 50 (inclusive). We could do this pretty easily:
my_list = range(51)
But what if we wanted to generate a list according to some logic—for example, a list of all the even numbers from 0 to 50?
Python's answer to this is the list comprehension.
List comprehensions are a powerful way to generate lists using the for/in and if keywords we've learned.
"""
# A list of all the even numbers from 0 to 50:
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50
print


# Here's a simple example of list comprehension syntax:
new_list = [x for x in range(1,6)]
print new_list
# => [1, 2, 3, 4, 5]
# This will create a new_list populated by the numbers one to five.

# If you want those numbers doubled, you could use:
doubles = [x*2 for x in range(1,6)]
print doubles
# => [2, 4, 6, 8, 10]

# And if you only wanted the doubled numbers that are evenly divisible by three:
doubles_by_3 = [x*2 for x in range(1,6) if (x*2)%3 == 0]
print doubles_by_3
# => [6]
print


# Use a list comprehension to build a list called even_squares in the editor.
# Your even_squares list should include the squares of the even numbers from 1 to 11.
# Your list should start [4, 16, 36...] and go from there.
even_squares = [i**2 for i in range(1,11) if i % 2 == 0]
print even_squares
print


# Great work! Now it's time for you to create a list comprehension all on your own.
c = ['C' for x in range(5) if x < 3]
print c
# The example above creates and prints out a list containing ['C', 'C', 'C']. (c[0], c[1], c[2])
print

# Use a list comprehension to create a list, cubes_by_four.
# The comprehension should consist of the cubes of the numbers 1 through 10 only if the cube is evenly divisible by four.
# Finally, print that list to the console.
# Note that in this case, the cubed number should be evenly divisible by 4, not the original number.
# Note to self -- if you want the numbers 1 to 10, use range(1,11)
cubes_by_four = [i**3 for i in range(1,11) if (i**3) % 4 == 0]
print cubes_by_four
print
