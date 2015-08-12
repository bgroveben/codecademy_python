# -*- coding: utf-8 -*-
"""
The while loop is similar to an if statement: it executes the code inside of it if some condition is true.
The difference is that the while loop will continue to execute as long as the condition is true.
In other words, instead of executing if something is true, it executes while that thing is true.
"""

count = 0

if count < 10:
    print "Hello, I am an if statement and count is", count
print

while count < 10:
    print "Hello, I am a while and count is", count
    count += 1
print


# The condition is the expression that decides whether the loop is going to be executed or not.
loop_condition = True

while loop_condition:
    print "I am a loop"
    loop_condition = False
print


# A common application of a while loop is to check user input to see if it is valid.
choice = raw_input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")
    # This loop will execute until you enter a correct choice.
print


"""
The break is a one-line statement that means "exit the current loop."
An alternate way to make our counting loop exit and stop executing is with the break statement.

First, create a while with a condition that is always true. The simplest way is shown.

Using an if statement, you define the stopping condition. Inside the if, you write break, meaning "exit the loop."

The difference here is that this loop is guaranteed to run at least once.
"""
count = 0

while True:
    print count
    count += 1
    if count >= 10:
        break
print


"""
Something completely different about Python is the while/else construction.
while/else is similar to if/else, but there is a difference: the else block will execute anytime the loop condition
is evaluated to False.
This means that it will execute if the loop is never entered or if the loop exits normally.
If the loop exits as the result of a break, the else will not be executed.

In this example, the loop will break if a 5 is generated, and the else will not execute.
Otherwise, after 3 numbers are generated, the loop condition will become false and the else will execute.
"""
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"
print


# In this exercise, allow the user to guess what the number is three times.
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)
# print random_number  ## for testing purposes
guesses_left = 3
# Start your game!
print "You get 3 chances to guess a number between 1 and 10."
while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    if guess == random_number:
        print 'You win!'
        break
    else:
        guesses_left -= 1
else:
    print 'You lose.'
