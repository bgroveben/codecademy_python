# Simple tip calculator. Codecademy went cheapskate; it should be 20%.

meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)
