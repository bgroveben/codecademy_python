# -*- coding: utf-8 -*-
print
"""
Until now, the Python code you've been writing comes from one source and only goes to one place: you type it in at the keyboard and its results are displayed in the console. But what if you want to read information from a file on your computer, and/or write that information to another file?

This process is called file I/O (the "I/O" stands for "input/output"), and Python has a number of built-in functions that handle this for you.
"""
my_list = [i**2 for i in range(1,11)]
# Generates a list of squares of the numbers 1 - 10

f = open("output.txt", "w")

for item in my_list:
    f.write(str(item) + "\n")

f.close()


# Finally, we want to know how to read from our output.txt file.
# As you might expect, we do this with the read() function, like so:
my_file = open("output.txt", "r")
print my_file.read()
my_file.close()
print


"""
What if we want to read from a file line by line, rather than pulling the entire file in at once. Thankfully, Python includes a readline() function that does exactly that.

If you open a file and call .readline() on the file object, you'll get the first line of the file; subsequent calls to .readline() will return successive lines.
"""
my_file = open("text.txt", "r")
print my_file.readline()
print my_file.readline()
print my_file.readline()
my_file.close()
print


"""
Programming is all about getting the computer to do the work. Is there a way to get Python to automatically close our files for us?

Of course there is. This is Python.

You may not know this, but file objects contain a special pair of built-in methods: __enter__() and __exit__(). The details aren't important, but what is important is that when a file object's __exit__() method is invoked, it automatically closes the file. How do we invoke this method? With with and as.
"""
# The syntax looks like this:

# with open("text.txt", "w") as textfile:
#    textfile.write("Success!")
# Running the above lines of code will overwrite text.txt.


"""
Finally, we'll want a way to test whether a file we've opened is closed. Sometimes we'll have a lot of file objects open, and if we're not careful, they won't all be closed. How can we test this?

f = open("bg.txt")
f.closed
# False
f.close()
f.closed
# True
Python file objects have a closed attribute which is True when the file is closed and False otherwise.

By checking file_object.closed, we'll know whether our file is closed and can call close() on it if it's still open.
"""
if not my_file.closed:  # if my_file.closed == False also works
    my_file.close()
print my_file.closed
print
