"""
CP1404/CP5632 - Practical
Student Name:Abid Hasan
Date:16/02/2025
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        is_finished=True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
