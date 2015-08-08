# Codecademy supermarket; keeping track of prices and inventory:

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

# Print out all of the inventory information:
for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]
print

# For paperwork and accounting purposes, let's record the total value of your inventory:
total = 0
for key in prices:
    print prices[key] * stock[key]
    total = total + (prices[key] * stock[key])
print total
