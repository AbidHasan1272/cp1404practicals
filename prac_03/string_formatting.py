"""
CP1404/CP5632 - Practical
Program: Various examples of using Python string formatting.
Student Name:Abid Hasan
Date:16/02/2025

"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.9

print(f"{year} {name} for about ${cost:,.0f}!")

for exponent in range(11):
    print(f"2 ^ {exponent:2} is {2**exponent:4}")

