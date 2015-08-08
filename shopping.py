shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# How much are we paying for the items on the shopping list?
def compute_bill(food):
    total = 0
    for item in food:
        if stock[item] > 0:  # If the item isn't in stock, don't include it in the total.
            total += prices[item]
            stock[item] -= 1
    return total

print compute_bill(shopping_list)
print stock
