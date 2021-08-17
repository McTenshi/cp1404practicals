"""
cp104 Practical
Shop Calculator
"""
"""
Pseudocode
get number_of_items
for number_of_items
    get price_of_item
    total_price += price_of_item
if total_price > DISCOUNT_THRESHOLD
    total_price = total_price - (total_price * 0.1)
print total_price
"""



DISCOUNT_THRESHOLD = 100
total_price = 0

number_of_items = int(input("Number of items: "))
for i in range(0, number_of_items):
    price_of_item = float(input("Price of items: "))
    while price_of_item < 0:
        print("Invalid price")
        price_of_item = float(input("Price of items: "))
    total_price += price_of_item
if total_price > DISCOUNT_THRESHOLD:
    total_price = total_price - (total_price * 0.1)
print(f"Total price for {number_of_items} items is ${total_price:0.2f}")
