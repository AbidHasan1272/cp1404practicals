"""
CP1404/CP5632 - Practical
Shop Calculator program
"""
number_of_items=int(input("Enter the number of items: "))
while number_of_items <=0:
    print("Invalid number of items")
    number_of_items = int(input("Enter the number of items: "))
total_price =0
price_of_item =0
for i in range (1,number_of_items+1,):
    price_of_item =float (input("Enter the price of the item: "))
    total_price += price_of_item
print(f"Total price for {number_of_items} items is $:{total_price:.2f}")