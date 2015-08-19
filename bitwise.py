# -*- coding: utf-8 -*-
print
"""
The next two operations we are going to talk about are the left and right shift bitwise operators. These operators work by shifting the bits of a number over by a designated number of slots.

The block below shows how these operators work on the bit level. Note that in the diagram, the shift is always a positive integer:

# Left Bit Shift (<<)
0b000001 << 2 == 0b000100 (1 << 2 = 4)
0b000101 << 3 == 0b101000 (5 << 3 = 40)

# Right Bit Shift (>>)
0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
0b0000010 >> 2 == 0b000000 (2 >> 2 = 0)
This operation is mathematically equivalent to floor dividing and multiplying by 2 (respectively) for every time you shift, but it's often easier just to think of it as shifting all the 1s and 0s left or right by the specified number of slots.

Note that you can only do bitwise operations on an integer. Trying to do them on strings or floats will result in nonsensical output!
"""
# Shift the variable shift_right to the right twice (>> 2) and shift the variable shift_left to the left twice (<< 2).
# Try to guess what the printed output will be!
shift_right = 0b1100
shift_left = 0b1

shift_right = shift_right >> 2
shift_left = shift_left << 2

print bin(shift_right)
print bin(shift_left)
print


"""
The bitwise AND (&) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if the corresponding bits of both numbers are 1. For example:

     a:   00101010   42
     b:   00001111   15
===================
 a & b:   00001010   10
As you can see, the 2's bit and the 8's bit are the only bits that are on in both a and b, so a & b only contains those bits. Note that using the & operator can only result in a number that is less than or equal to the smaller of the two values.

So remember, for every given bit in a and b:

0 & 0 = 0
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1
Therefore,

 0b111 (7) & 0b1010 (10) = 0b10
which equals two.
"""
# Print out the result of calling bin() on 0b1110 & 0b101.
print bin(0b1110 & 0b101)
print 0b1110 & 0b101
print


"""
The bitwise OR (|) operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of either number are 1. For example:

    a:  00101010  42
    b:  00001111  15
================
a | b:  00101111  47
Note that the bitwise | operator can only create results that are greater than or equal to the larger of the two integer inputs.

So remember, for every given bit in a and b:

0 | 0 = 0
0 | 1 = 1
1 | 0 = 1
1 | 1 = 1
Meaning

 110 (6) | 1010 (10) = 1110 (14)
"""
# For practice, print out the result of using | on 0b1110 and 0b101 as a binary string.
# Try to do it on your own without using the | operator if you can help it.
print bin(0b1110 | 0b101)
print 0b1110 | 0b101
print 0b1111
print


"""
The XOR (^) or exclusive or operator compares two numbers on a bit level and returns a number where the bits of that number are turned on if either of the corresponding bits of the two numbers are 1, but not both.

    a:  00101010   42
    b:  00001111   15
================
a ^ b:  00100101   37
Keep in mind that if a bit is off in both numbers, it stays off in the result. Note that XOR-ing a number with itself will always result in 0.

So remember, for every given bit in a and b:

0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
Therefore:

 111 (7) ^ 1010 (10) = 1101 (13)
"""
# For practice, print the result of using ^ on 0b1110 and 0b101 as a binary string.
print bin(0b1110 ^ 0b101)
print 0b1110 ^ 0b101
print 0b1011
print


"""
The bitwise NOT operator (~) just flips all of the bits in a single number. What this actually means to the computer is actually very complicated, so we're not going to get into it. Just know that mathematically, this is equivalent to adding one to the number and then making it negative.
"""
print ~1
print ~2
print ~3
print ~42
print ~123
print
print bin(1)
print bin(~1)
print bin(2)
print bin(~2)
print bin(3)
print bin(~3)
print bin(42)
print bin(~42)
print bin(123)
print bin(~123)
print
