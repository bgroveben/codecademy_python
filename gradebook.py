# Time to teach your own class.
# Make a gradebook for all of your students.
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# Create a list called students that contains lloyd, alice, and tyler.
students = [lloyd, alice, tyler]
# For each student in your students list, print out that student's data.
for student in students:
    print student["name"]
    print student["homework"]
    print student["quizzes"]
    print student["tests"]

# Write a function average that takes a list of numbers and returns the average.
def average(numbers):
    total = sum(numbers)
    total = float(total)
    return total / len(numbers)
# print average(tyler["tests"])  # => 100.0
# print average(alice["homework"])  # => 97.5

# Write a function called get_average that takes a student dictionary as input and returns his/her weighted average.
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return (0.1 * homework) + (0.3 * quizzes) + (0.6 * tests)

print get_average(tyler)  # => 79.9
print get_average(alice)  # => 91.15
print get_average(lloyd)  # => 80.55
