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


