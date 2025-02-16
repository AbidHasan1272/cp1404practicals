"""
CP1404/CP5632 - Practical
Program: Capitalist Conrad wants a stock price simulator for a volatile stock.
Student Name:Abid Hasan
Date:16/02/2025

"""
import random

MAX_INCREASE = 0.175  # 17.5%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 1
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
FILENAME = "stock_prices.txt"

price = INITIAL_PRICE
number_of_days =0
out_file = open(FILENAME, 'w')
print(f"Starting price: ${price:,.2f}")
print(f"Starting price: ${price:,.2f}", file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    number_of_days += 1
    price_change = 0

    if random.randint(1, 2) == 1:
        price_change = random.uniform(0, MAX_INCREASE)  # Increase
    else:
        price_change = random.uniform(-MAX_DECREASE, 0)  # Decrease

    price *= (1 + price_change)

    # Print and write daily price update
    print(f"On day {number_of_days} price is: ${price:,.2f}")
    print(f"On day {number_of_days} price is: ${price:,.2f}", file=out_file)

# Closing the file
out_file.close()

print(f"Prices saved to {FILENAME}.")
