"""
The range function has three different versions:

range(stop)
range(start, stop)
range(start, stop, step)
"""

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(3))  # => [0, 2, 4]
print


"""
Now that we've learned about range, we have two ways of iterating through a list.

Method 1 - for item in list:
for item in list:
    print item

Method 2 - iterate through indexes:
for i in range(len(list)):
    print list[i]

Method 1 is useful to loop through the list, but it's not possible to modify the list this way.
Method 2 uses indexes to loop through the list, making it possible to also modify the list if needed.
Since we aren't modifying the list, feel free to use either one on this lesson!
"""

n = [3, 5, 7]

def total(numbers):
    result = 0
    for i in range(len(numbers)):
        result += numbers[i]
    return result

print total(n)  # => 15
print


# Neat! Let's try it with strings.
n = ["Michael", "Lieberman"]

def join_strings(words):
    result = ""
    for w in range(len(words)):
        result += words[w]  # Why not append? Because "AttributeError: 'str' object has no attribute 'append'"
    return result

print join_strings(n)  # => MichaelLieberman
print


# Now let's make stuff a bit more complicated.
# Create a function called flatten that takes a single list and concatenates all of the sublists into a single list.
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def flatten(lists):
    results = []
    for numbers in lists:  # Method 1 from above
        for num in range(len(numbers)):  # Method 2 from above. Isn't learning fun?
            results.append(numbers[num])
    return results

print flatten(n)  # => [1, 2, 3, 4, 5, 6, 7, 8, 9]

