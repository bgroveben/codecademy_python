# -*- coding: utf-8 -*-
# An integer is just a number without a decimal part (for instance, -17, 0, and 42 are all integers, but 98.6 is not).
# For the purpose of this lesson, we'll also say that a number with a decimal part that is all 0s is also an integer, such as 7.0.
# Define a function is_int that takes a number x as an input.
# Have it return True if the number is an integer (as defined above) and False otherwise.
def is_int(x):
    if round(x) - x != 0:
        return False
    else:
        return True

print is_int(1)
print is_int(1.7)
print


# Write a function called digit_sum that takes a positive integer n as input and returns the sum of all that number's digits.
# For example: digit_sum(1234) should return 10 which is 1 + 2 + 3 + 4.
# Assume that the number you are given will always be positive.
def digit_sum(n):
    total = 0
    for x in str(n):
        total += int(x)
    return total

print digit_sum(1234)
print


# Calculate the factorial of a non-negative integer x.
# Define a function factorial that takes an integer x as input.
# Calculate and return the factorial of that number.
#!# NOT using from math import factorial #!#
def factorial(x):
    if x < 2:  # if x == 0 also works
        return 1
    else:
        return x * factorial(x - 1)

print factorial(9)
print


# Define a function called is_prime that takes a number x as input.
# For each number n from 2 to x - 1, test if x is evenly divisible by n.
# If it is, return False.
# If none of them are, then return True
def is_prime(x):
    if x < 2:
        return False
    else:
        for i in range(2, x):
            if x % i == 0:
                return False
        return True

print is_prime(47)
