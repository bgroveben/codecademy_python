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
print


# Define a function called reverse that takes a string textand returns that string in reverse.
# For example: reverse("abcd") should return "dcba".
# You may not use reversed or [::-1] to help you with this.
# You may get a string containing special characters (for example, !, @, or #).
def reverse(text):
    forwards = []
    backwards = []
    for letter in text:
        forwards.append(letter)
    while len(forwards) > 0:
        backwards.append(forwards.pop())
    return ''.join(map(str, backwards))

print reverse("Python!")
# This function is shorter and works as well:
def reverse(text):
    ab = []
    a = list(text)
    for i in a:
        ab.insert(0,i)
    s = ""
    return s.join(ab)

print reverse("Python")
print reverse("Monty")
print


# Define a function called anti_vowel that takes one string, text, as input and returns the text with all of the vowels removed.
# For example: anti_vowel("Hey You!") should return "Hy Y!".
# Don't count Y as a vowel.
# Make sure to remove lowercase and uppercase vowels.
def anti_vowel(text):
    new_text = text
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    for letter in text:
        if letter in vowels:
            new_text = new_text.replace(letter, "")
    return new_text

print anti_vowel("Hey You!")
# A slightly simpler solution:
def anti_vowel(text):
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'I', 'E', 'O', 'U')
    for char in text:
        if char in vowels:
            text = text.replace(char, '')
    return text

print anti_vowel("Hey You!")
# This is the more 'pythonic' way to do it, according to a S.O. post:
def anti_vowel(text):
    vowels = ('a','e','i','o','u','A','E','I','O','U')
    return ''.join([x for x in text if x not in vowels])

print anti_vowel("Hey You!")
print


# Define a function scrabble_score that takes a string word as input and returns the equivalent scrabble score for that word.
# Assume your input is only one word containing no spaces or punctuation.
# As mentioned, no need to worry about score multipliers!
# Your function should work even if the letters you get are uppercase, lowercase, or a mix.
# Assume that you're only given non-empty strings.
def scrabble_score(word):
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
             "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
             "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
             "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}
    word = word.lower()
    total = 0
    for letter in word:
        for key, value in score.iteritems():
            if letter == key:
                total += value
    return total
# There is probably a more elegant way to do this, but just getting it to work is enough for now.
print scrabble_score("Helix")
print


# Write a function called censor that takes two strings, text and word, as input.
# It should return the text with the word you chose replaced with asterisks.
# For example:
# censor("this hack is wack hack", "hack") should return:
# "this **** is wack ****"
# Assume your input strings won't contain punctuation or upper case letters.
# The number of asterisks you put should correspond to the number of letters in the censored word.
def censor(text, word):
    new_text = []
    text = text.split()
    for w in text:
        if w == word:
            new_text.append("*" * len(w))
        else:
            new_text.append(w)
    return " ".join(new_text)

print censor("this hack is wack hack", "hack")
print


# Define a function called count that has two arguments called sequence and item.
# Return the number of times the item occurs in the list.
# For example: count([1,2,1,1], 1) should return 3 (because 1 appears 3 times in the list).
# There is a list method in Python that you can use for this, but you should do it the long way for practice.
# Your function should return an integer.
# The item you input may be an integer, string, float, or even another list!
# Be careful not to use list as a variable name in your code—it's a reserved word in Python!
def count(sequence, item):
    total = 0
    for x in sequence:
        if x == item:
            total += 1
    return total

print count([1,2,1,1], 1)
print


# Define a function called purify that takes in a list of numbers, removes all odd numbers in the list, and returns the result.
# For example, purify([1,2,3]) should return [2].
# Do not directly modify the list you are given as input; instead, return a new list with only the even numbers.
def purify(numbers):
    new_numbers = []
    for i in numbers:
        if i % 2 == 0:
            new_numbers.append(i)
    return new_numbers

print purify([1,2,3,4])
# The more pythonic way:
def purify(numbers):
    return [i for i in numbers if i % 2 == 0]

print purify([1,2,3,4])
print


# Define a function called product that takes a list of integers as input and returns the product of all of the list elements.
# For example: product([4, 5, 5]) should return 100 (because 4 * 5 * 5 is 100).
# Don't worry about the list being empty.
# Your function should return an integer.
def product(numbers):
    total = 1
    for i in numbers:
        total *= i
    return total

print product([4,5,5])
print


# Write a function remove_duplicates that takes in a list and removes elements of the list that are the same.
# For example: remove_duplicates([1,1,2,2]) should return [1,2].
# Don't remove every occurrence, since you need to keep a single occurrence of a number.
# The order in which you present your output does not matter. So returning [1,2,3] is the same as returning [3,1,2].
# Do not modify the list you take as input! Instead, return a new list
def remove_duplicates(elements):
    new_list = []
    for i in elements:
        if i not in new_list:
            new_list.append(i)
    return new_list

print remove_duplicates([1,1,2,2])
# A more elegant solution:
def remove_duplicates(some_list):
    new_list = []
    [new_list.append(x) for x in some_list if x not in new_list]
    return new_list

print remove_duplicates([1,1,2,2])
print


# Write a function called median that takes a list as an input and returns the median value of the list.
# For example: median([1,1,2]) should return 1.
# The list can be of any size and the numbers are not guaranteed to be in any particular order.
# If the list contains an even number of elements, your function should return the average of the middle two.
"""
Great work! You've covered a lot in these exercises. Last but not least, let's write a function to find the median of a list.

The median is the middle number in a sorted sequence of numbers.

Finding the median of [7,12,3,1,6] would first consist of sorting the sequence into [1,3,6,7,12] and then locating the middle value, which would be 6.

If you are given a sequence with an even number of elements, you must average the two elements surrounding the middle.

For example, the median of the sequence [7,3,1,4] is 3.5, since the middle elements after sorting the list are 3 and 4 and (3 + 4) / (2.0) is 3.5.

You can sort the sequence using the sorted() function, like so:

sorted([5, 2, 3, 1, 4])
[1, 2, 3, 4, 5]
"""
def median(some_list):
    sorted_list = sorted(some_list)
    for i in sorted_list:
        if len(sorted_list) % 2 != 0:
            return sorted(sorted_list)[len(sorted_list)/2]  # Floor division is default in Python 2; Python 3 requires //.
        else:
            return float(sum(sorted_list[(len(sorted_list)/2)-1:(len(sorted_list)/2)+1]))/2.0

print median([1,1,2])
print median([7,3,1,4])
print
