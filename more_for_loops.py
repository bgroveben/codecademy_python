# -*- coding: utf-8 -*-
# This kind of loop is useful when you want to do something a certain number of times, such as append something to the end of a list.
hobbies = []
for i in range(3):
    hobby = str(raw_input("What is your hobby? "))
    hobbies.append(hobby)
print hobbies
print


# Using a for loop, you can print out each individual character in a string.
thing = "spam!"
for c in thing:
    print c
print
word = "eggs!"
for letter in word:
    print letter
print


# String manipulation is useful in for loops if you want to modify some content in a string.
# Let's filter out the letter 'A' from our string.
phrase = "A bird in the hand..."
for char in phrase:
    if char == 'A' or char == 'a':
        print 'X',
    else:
        print char,
print
print


# You may be wondering how looping over a dictionary would work. Would you get the key or the value?
# The short answer is: you get the key which you can use to get the value.
d = {'x': 9, 'y': 10, 'z': 20}
for key in d:
    if d[key] == 10:
        print "This dictionary has the value 10!"
print

d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}

for key in d:
    print key, d[key]
print


"""
A weakness of using this for-each style of iteration is that you don't know the index of the thing you're looking at. Generally this isn't an issue, but at times it is useful to know how far into the list you are. Thankfully the built-in enumerate function helps with this.

enumerate works by supplying a corresponding index to each element in the list that you pass it. Each time you go through the loop, index will be one greater, and item will be the next item in the sequence. It's very similar to using a normal for loop with a list, except this gives us an easy way to count how many items we've seen so far.
"""
# We don't want the user to see things listed from index 0, since this looks unnatural.
# Instead, the items should appear to start at index 1.
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
    print (index + 1), item
print


# zip will create pairs of elements when passed two lists, and will stop at the end of the shorter list.
# zip can handle three or more lists as well!
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    if a > b:
        print a
    else:
        print b
print



# Just like with while, for loops may have an else associated with them.
# In this case, the else statement is executed after the for, but only if the for ends normally—that is, not with a break.
# This code will break when it hits 'tomato', so the else block won't be executed.
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':  # Change this to something not in the list and see what happens.
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'
print


# Build your for/else statement in the editor.
# Execution of the else branch is optional, but your code should print a string of your choice to the editor regardless.
languages = ["python", "ruby", "javascript", "php"]
for l in languages:
    if l == "scala":
        print "Codecademy doesn't teach scala."
        break
    print "Codecademy teaches " + l
else:
    print "Codecademy teaches coding."
print
