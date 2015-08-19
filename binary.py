# -*- coding: utf-8 -*-
print
"""
Bitwise operations are operations that directly manipulate bits.
In all computers, numbers are represented with bits, a series of zeros and ones.
In fact, pretty much everything in a computer is represented by bits.
This course will introduce you to the basic bitwise operations and then show you what you can do with them.
"""
print 5 >> 4  # Right Shift  => 0
print 5 << 1  # Left Shift   => 10
print 8 & 5   # Bitwise AND  => 0
print 9 | 4   # Bitwise OR   => 13
print 12 ^ 42 # Bitwise XOR  => 38
print ~88     # Bitwise NOT  => -89
print

"""
When we count, we usually do it in base 10. That means that each place in a number can hold one of ten values, 0-9. In binary we count in base two, where each place can hold one of two values: 0 or 1. The counting pattern is the same as in base 10 except when you carry over to a new column, you have to carry over every time a place goes higher than one (as opposed to higher than 9 in base 10).

For example, the numbers one and zero are the same in base 10 and base 2. But in base 2, once you get to the number 2 you have to carry over the one, resulting in the representation "10". Adding one again results in "11" (3) and adding one again results in "100" (4).

Contrary to counting in base 10, where each decimal place represents a power of 10, each place in a binary number represents a power of two (or a bit). The rightmost bit is the 1's bit (two to the zero power), the next bit is the 2's bit (two to the first), then 4, 8, 16, 32, and so on.

The binary number '1010' is 10 in base 2 because the 8's bit and the 2's bit are "on":

8's bit  4's bit  2's bit  1's bit
    1       0       1      0
    8   +   0    +  2   +  0  = 10
In Python, you can write numbers in binary format by starting the number with 0b. When doing so, the numbers can be operated on like any other number!
"""
print 0b1,    #1
print 0b10,   #2
print 0b11,   #3
print 0b100,  #4
print 0b101,  #5
print 0b110,  #6
print 0b111   #7
print "******"
print 0b1 + 0b11
print 0b11 * 0b11
print


# Fill out the rest of the numbers with their corresponding binary values up to twelve in the editor to the right,
# using the 0bxxx format.
one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100
print [0b1, 0b10, 0b11, 0b100, 0b101, 0b110, 0b111, 0b1000, 0b1001, 0b1010, 0b1011, 0b1100]
print


"""
Excellent! The biggest hurdle you have to jump over in order to understand bitwise operators is learning how to count in base 2. Hopefully the lesson should be easier for you from here on out.

There are Python functions that can aid you with bitwise operations. In order to print a number in its binary representation, you can use the bin() function. bin() takes an integer as input and returns the binary representation of that integer in a string. (Keep in mind that after using the bin function, you can no longer operate on the value like a number.)

You can also represent numbers in base 8 and base 16 using the oct() and hex() functions. (We won't be dealing with those here, however.)
"""
# We've provided an example of the bin function in the editor.
# Go ahead and use print and bin() to print out the binary representations of the numbers 2 through 5, each on its own line.
print bin(1)
print bin(2)
print bin(3)
print bin(4)
print bin(5)
print bin(6)
print


"""
Python has an int() function that you've seen a bit of already. It can turn non-integer input into an integer, like this:

int("42")
# ==> 42
What you might not know is that the int function actually has an optional second parameter.

int("110", 2)
# ==> 6
When given a string containing a number and the base that number is in, the function will return the value of that number converted to base ten.
"""
# In the console are several different ways that you can use the int function's second parameter.
print int("1",2)
print int("10",2)
print int("111",2)
print int("0b100",2)
print int(bin(5),2)
# Use int to print the base 10 equivalent of the binary number 11001001.
print int("11001001",2)
print
