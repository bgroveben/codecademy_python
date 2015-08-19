# -*- coding: utf-8 -*-
print
"""
A bit mask is just a variable that aids you with bitwise operations. A bit mask can help you turn specific bits on, turn others off, or just collect data from an integer about which bits are on or off.

num  = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
    print "Bit was on"
In the example above, we want to see if the third bit from the right is on.

First, we first create a variable num containing the number 12, or 0b1100.
Next, we create a mask with the third bit on.
Then, we use a bitwise-and operation to see if the third bit from the right of num is on.
If desired is greater than zero, then the third bit of num must have been one.
"""
# Define a function, check_bit4, with one argument, input, an integer.
# It should check to see if the fourth bit from the right is on.
# If the bit is on, return "on" (not print!)
# If the bit is off, return "off".
def check_bit4(input):
    mask = 0b1000
    desired = input & mask
    if desired > 0:
        return "on"
    else:
        return "off"

print check_bit4(0b0)
print check_bit4(0b1100)
print check_bit4(0b10110)
print check_bit4(0b11100)
print


"""
You can also use masks to turn a bit in a number on using |. For example, let's say I want to make sure the rightmost bit of number a is turned on. I could do this:

a = 0b110  # 6
mask = 0b1  # 1
desired =  a | mask  # 0b111, or 7
Using the bitwise | operator will turn a corresponding bit on if it is off and leave it on if it is already on.
"""
# In the editor is a variable, a.
# Use a bitmask and the value a in order to achieve a result where the third bit from the right of a is turned on.
# Be sure to print your answer as a bin() string!
a = 0b10111011
mask = 0b100
print bin(a | mask)
print a | mask
print


"""
Using the XOR (^) operator is very useful for flipping bits. Using ^ on a bit with the number one will return a result where that bit is flipped.

For example, let's say I want to flip all of the bits in a. I might do this:

a = 0b110 # 6
mask = 0b111 # 7
desired =  a ^ mask # 0b1
"""
# In the editor is the 8 bit variable a.
# Use a bitmask and the value a in order to achieve a result where all of the bits in a are flipped.
# Be sure to print your answer as a bin() string!
a    = 0b11101110
mask = 0b11111111
print bin(a ^ mask)
print a ^ mask
print


"""
Finally, you can also use the left shift (<<) and right shift (>>) operators to slide masks into place.

a = 0b101
# Tenth bit mask
mask = (0b1 << 9)  # One less than ten
desired = a ^ mask
Let's say that I want to turn on the 10th bit from the right of the integer a.

Instead of writing out the entire number, we slide a bit over using the << operator.

We use 9 because we only need to slide the mask nine places over from the first bit to reach the tenth bit.
"""
# Define a function called flip_bit that takes the inputs (number, n).
# Flip the nth bit (with the ones bit being the first bit) and store it in result.
# Return the result of calling bin(result).
def flip_bit(number, n):
    mask = (0b1 << (n - 1))
    result = number ^ mask
    return bin(result)

print flip_bit(0b101, 2)
print flip_bit(0b1011, 3)
print flip_bit(0b1001011, 3)
print

