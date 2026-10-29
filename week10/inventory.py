
# Reflection 1:
# I was surprised by how easily Python lets us access items from the end of a list
# using negative numbers. I also did not expect slicing to make it so simple to
# select multiple items without writing a loop.

# Reflection 2:
# In the Investment Club, I work with financial information from different
# companies and periods. Python lists could make it easier to organize those
# numbers, calculate averages, and filter results instead of doing everything
# manually in Excel.


# Exercise 1: Build the list
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print("Exercise 1")
print(inventory)
print(len(inventory))


# Exercise 2: Index practice
print("\nExercise 2")
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])


# Exercise 3: Slicing
print("\nExercise 3")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# Exercise 4: Modify
print("\nExercise 4")
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)


# Exercise 5: Tuple comparison
print("\nExercise 5")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples cannot be changed, which makes them useful for coordinates.")

print(coords)


# Exercise 6: Average of a list of sales
print("\nExercise 6")
sales = [100, 250, 75, 480, 200]

print("Total:", sum(sales))
print("Count:", len(sales))
print("Average:", sum(sales) / len(sales))
print("Best:", max(sales))
print("Worst:", min(sales))


# Exercise 7: Accumulator pattern
print("\nExercise 7")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print("Original:", prices)
print("Discounted:", discounted)


# Exercise 8: Filter above threshold
print("\nExercise 8")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print("High sales:", high_sales)
print("Count:", len(high_sales))
print("Average:", sum(high_sales) / len(high_sales))
  