"""
List Slicing Syntax
Sometimes we only want part of a Python list.
Maybe we only want the first few elements; maybe we only want the last few.
Maybe we want every other element!
List slicing allows us to access elements of a list in a concise manner. The syntax looks like this:

[start:end:stride]

Where start describes where the slice starts (inclusive), end is where it ends (exclusive), and stride
describes the space between items in the sliced list.
For example, a stride of 2 would select every other item from the original list to place in the sliced list.
"""
l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print l[2:9:2]
# => [9, 25, 49, 81]
print


# If you don't pass a particular index to the list slice, Python will pick a default.
to_five = ['A', 'B', 'C', 'D', 'E']
print to_five[3:]
# prints ['D', 'E']
print to_five[:2]
# prints ['A', 'B']
print to_five[::2]
# print ['A', 'C', 'E']
# The default starting index is 0.
# The default ending index is the end of the list.
# The default stride is 1.
print


# Use list slicing to print out every odd element of my_list from start to finish.
# Omit the start and end index. You only need to specify a stride.
my_list = range(1, 11) # List of numbers 1 - 10
print my_list[::2]
print


# We have seen that a positive stride progresses through the list from left to right.
# A negative stride progresses through the list from right to left.
letters = ['A', 'B', 'C', 'D', 'E']
print letters[::-1]
# In the example above, we print out ['E', 'D', 'C', 'B', 'A'].
print


# Create a variable called backwards and set it equal to the reversed version of my_list.
# Make sure to reverse the list in the editor by passing your list slice a negative stride, like in the example above.
my_list = range(1, 11)
backwards = my_list[::-1]
print backwards
print


# Create a variable, backwards_by_tens, and set it equal to the result of going backwards through to_one_hundred by tens.
# Go ahead and print backwards_by_tens to the console.
to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens
print


# Create a list, to_21, that's just the numbers from 1 to 21, inclusive.
# Create a second list, odds, that contains only the odd numbers in the to_21 list (1, 3, 5, and so on).
# Use list slicing for this one instead of a list comprehension.
# Finally, create a third list, middle_third, that's equal to the middle third of to_21, from 8 to 14, inclusive.
to_21 = range(1,22)
print to_21
odds = to_21[::2]
print odds
middle_third = to_21[7:14]
print middle_third
print
