# Advanced topics in Python

for number in range(5):
    print number,

d = { "name": "Eric", "age": 26 }
for key in d:
    print key, d[key],

for letter in "Eric":
    print letter,  # Note the comma! Leaving the commas in means the output will be printed on the same line

print
print


my_dict = {
    "Name": "Ben",
    "Age": "Still young",
    "Hobby": "Programming"
}
print my_dict.keys()
print my_dict.values()

for key in my_dict:
    print key, my_dict[key]

print
