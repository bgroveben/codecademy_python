# -*- coding: utf-8 -*-
"""
Anonymous Functions
One of the more powerful aspects of Python is that it allows for a style of programming called functional programming,
which means that you're allowed to pass functions around just as if they were variables or values.
Sometimes we take this for granted, but not all languages allow this!

Check out the code at the right. See the lambda bit? Typing

lambda x: x % 3 == 0

Is the same as

def by_three(x):
    return x % 3 == 0

Only we don't need to actually give the function a name; it does its work and returns a value without one.
That's why the function the lambda creates is an anonymous function.

When we pass the lambda to filter, filter uses the lambda to determine what to filter, and the second argument
(my_list, which is just the numbers 0 – 15) is the list it does the filtering on.
"""
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)
print


# Lambdas are useful when you need a quick function to do some work for you.
# If you plan on creating a function you'll use over and over, you're better off using def and giving that function a name.

# Fill in the first part of the filter function with a lambda.
# The lambda should ensure that only "Python" is returned by the filter.
# Fill in the second part of the filter function with languages, the list to filter.
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)
print


# Create a list, squares, that consists of the squares of the numbers 1 to 10. A list comprehension could be useful here!
# Use filter() and a lambda expression to print out only the squares that are between 30 and 70 (inclusive).
squares = [x**2 for x in range(1, 11)]
print filter(lambda x: x >= 30 and x <= 70, squares)
# print filter(lambda x: 30 <= x <= 70, squares)  # This also works.
print
