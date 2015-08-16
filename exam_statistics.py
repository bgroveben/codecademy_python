# -*- coding: utf-8 -*-

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

# First, let's write a function that prints all of the grades (I know, I know).
def print_grades(grades):
    for grade in grades:
        print grade  # This will print each grade on its own line.
    return grades  # This will print a list of all of the grades

print print_grades(grades)
print


# Compute the sum of all of the test grades.
# No, we're not using the sum() function.
def grades_sum(scores):
    total = 0
    for score in scores:
        total += score
    return total

print grades_sum(grades)
print


# Define a function grades_average(), below the grades_sum() function that does the following:
# Has one argument, grades, a list
# Calls grades_sum with grades
# Computes the average of the grades by dividing that sum by float(len(grades)).
# Returns the average.
# Call the newly created grades_average() function with the list of grades and print the result.
def grades_average(grades):
    return grades_sum(grades) / float(len(grades))

print grades_average(grades)
print


"""
Let's see how the grades varied against the average. This is called computing the variance.
A very large variance means that the students' grades were all over the place, while a small variance
(relatively close to the average) means that the majority of students did fairly well.
"""
# Define a new function called grades_variance() that accepts one argument, scores, a list.
# First, create a variable average and store the result of calling grades_average(scores).
# Next, create another variable variance and set it to zero. We will use this as a rolling sum.
# For each score in scores: Compute its squared difference: (average - score) ** 2 and add that to variance.
# Divide the total variance by the number of scores.
# Then, return that result.
# Finally, after your function code, print grades_variance(grades).
def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return variance / len(scores)

print grades_variance(grades)
print


"""
Great job computing the variance! The last statistic will be much simpler: standard deviation.
The standard deviation is the square root of the variance.
You can calculate the square root by raising the number to the one-half power.
"""
# Define a function grades_std_deviation(variance).
# Return the result of variance ** 0.5
# After the function, create a new variable called variance and store the result of calling grades_variance(grades).
# Finally print the result of calling grades_std_deviation(variance).
def grades_std_deviation(variance):
    return variance ** 0.5

variance = grades_variance(grades)
print grades_std_deviation(variance)
print
