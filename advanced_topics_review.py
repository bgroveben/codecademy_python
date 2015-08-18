# -*- coding: utf-8 -*-
print
# First, let's review iterating over a dict.
# Call the appropriate method on movies such that it will print out all the items (hint, hint) in the dictionary—
# that is, each key and each value.
movies = {
    "Monty Python and the Holy Grail": "Great",
    "Monty Python's Life of Brian": "Good",
    "Monty Python's Meaning of Life": "Okay"
}
print movies.items()
print


# Good! Now let's take another look at list comprehensions.
# squares = [x**2 for x in range(5)]
#Use a list comprehension to create a list, threes_and_fives, that consists only of the numbers between 1 and
# 15 (inclusive) that are evenly divisible by 3 or 5.
threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]
print threes_and_fives
print


# Great! Next up: list slicing.

# str = "ABCDEFGHIJ"
# start, end, stride = 1, 6, 2
# str[start:end:stride]

# You can think of a Python string as a list of characters.
# The string in the editor is garbled in two ways:
# First, our message is backwards;
# Second, the letter we want is every other letter.
# Use list slicing to extract the message and save it to a variable called message.
garbled = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
message = garbled[::-2]
print message
print


# Last but not least, let's look over some lambdas.
# my_list = range(16)
# filter(lambda x: x % 3 == 0, my_list)
# We've given you another (slightly different) garbled. Sort it out with a filter() and a lambda.

# Create a new variable called message.
# Set it to the result of calling filter() with the appropriate lambda that will filter out the "X"s.
# The second argument will be garbled.
# Finally, print your message to the console.
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X", garbled)
print message
print
