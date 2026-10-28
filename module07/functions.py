# The first bug I spotted was there was no : after the for sales in sales loop. I found it in the tracebook. It tells me I can see when I miss an important character. 
# apply_discount(price, tier) means that apply_discount will look at the price and then the tier. If it falls in the right spot, python will apply the discount. 
# My AI disclosure message: I used ChatGPT to help me identify what was the error in my code for the error (sales[i]). The AI built my understanding of simple rules in python such as python indexes lists from 0 so the original code was not following that rule. 

# --- Exercise 1 ---

# Define calculate tax function

def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7% is: ${tax1:.2f}") # 7.00
print(f"Tax on $250 at 8% is: ${tax2:.2f}") # 20.00
print(f"Another Tx: ${calculate_tax(500, 0.05):.2f}") # 7.50

# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

    # Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# --- Exercise 3 ---

# Write it out manually first, then refactor to a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${after_tax:.2f}")

# Refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax


print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# --- Exercise 4 ---

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders: 
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")


# --- Exercise 6 ---

x = 100 # Global

def double_it():
    global x
    x = 999 # Local
    return x * 2

print(x)
print(double_it())
print(x)

# --- Exercise 5 ---
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total = sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1
print("Done printing sales.")
