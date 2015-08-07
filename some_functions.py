def cube(number):
    return number * number * number

def by_three(number):
    if number % 3 == 0:
        return cube(number)
    else:
        return False

print cube(9)
print by_three(15)
print by_three(7)
print


def shut_down(s):
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"

print shut_down("yes")
print shut_down("no")
print shut_down("spam")
print


def distance_from_zero(n):
    if type(n) == int or type(n) == float:
        return abs(n)
    else:
        return "Nope"

print distance_from_zero(-42)
print distance_from_zero(-4.2)
print distance_from_zero("spam")
