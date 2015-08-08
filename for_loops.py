# For loop for a list:
names = ["Adam","Alex","Mariah","Martine","Columbus"]
for name in names:
    print name
print


# For loop for a dictionary:
# Use a for loop to go through the webster dictionary and print out all of the definitions.
webster = {
    "Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}
for word in webster:
    print webster[word]
print


# Print even numbers in a list:
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
for number in a:
    if number % 2 == 0:
        print number
print


# Using a for loop in a function that takes a list as input:
def fizz_count(x):
    count = 0
    for item in x:
        if item == "fizz":
            count = count + 1
            # count += 1 also works
    return count

print fizz_count(["fizz","cat","fizz"])
print


# Looping through a string:
for letter in "Codecademy":
    print letter

# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print letter
print
