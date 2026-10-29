# Self Assesment Questions:
# Question 1:
# The first bug I noticed was the missing colon in the for loop, which caused a SyntaxError. 
# After that, I noticed another problem with the while loop that was causing an IndexError. 
# I used VS Code and ChatGPT to understand what the errors meant and tried different solutions before correcting them. 
# I think this showed me that I am starting to recognize errors, but I still need more practice understanding exactly what 
# causes them and how to fix them independently.
#
# Question 2:
# The function calculates the final price of a product after applying a discount based on the customer's tier. 
# It takes two inputs: the original price and the customer's tier. Depending on whether the customer is gold, silver, 
# bronze, or none, it applies a discount of 15%, 10%, 5%, or 0%. It then returns the new price after the discount. 
# I think a colleague could understand its purpose from the function name and parameters, although adding a docstring 
# would make it easier to use without reading the code.
#
# Question 3:
# AI Use Disclosure: I used ChatGPT to help me understand Python concepts, review my code, and explain error messages 
# during the lab.
# I think using AI helped me understand the material better, especially how functions work together and how to identify 
# errors. I tried writing most of the exercises myself before asking for help. There were moments when AI gave me more of the 
# solution than I needed, but overall, it helped me understand why certain parts of my code were incorrect instead of just giving 
# me answers.

# - Exercise 1 -
def calculate_tax(price, rate):
    return price*rate
tax = calculate_tax(100, 0.07)
print(f"Tax on $100 at 7%: ${tax:.2f}")
tax = calculate_tax(250, 0.08)
print(f"Tax on $250 at 8%: ${tax:.2f}")

# - Exercise 2 -
def apply_discount(price, tier):
    if tier == "gold":
        discount= 0.15
    elif tier == "silver":
        discount= 0.10
    elif tier == "bronze":
        discount= 0.05
    else:
        discount=0
    return price*(1-discount)

tiers=["gold","silver","bronze","none"]
for tier in tiers:
    new_price=apply_discount(200, tier)
    print(f'{tier}: ${new_price:.2f}')

# - Exercise 3 -
tier = input("Enter your customer tier: ").lower()
price= 200.00
tax_rate=0.07
def final_price(price,tier,tax_rate):
    discounted_price=apply_discount(price, tier)
    print(f'After {tier} discount: ${discounted_price:.2f}')
    tax=calculate_tax(discounted_price, tax_rate)
    price_after_tax=discounted_price+tax
    print(f"After tax: ${price_after_tax:.2f}")
    return price_after_tax
ending_price=final_price(price,tier,tax_rate)
print(f'final_price({price}, "{tier}", {tax_rate}) = {ending_price:.2f}')

# - Exercise 4 -
orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, tax_rate)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# - Exercise 5 -
sales = [120, 80, 250, 175, 90]
total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
        print(sales[i])
        i+=1

# - Exercise 6 -
x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # what prints here? I think it's gonna print the global x
print(double_it()) # what prints here? It will print 999 * 2 which is 1998
print(x)           # has x changed? I'm not sure but I think it should be 100 again
