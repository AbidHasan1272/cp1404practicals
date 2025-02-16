"""
CP1404/CP5632 - Practical
Student Name:Abid Hasan
Date:16/02/2025
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")


# When will a ValueError occur?
# Answer:If the user enters anything(str,float) other than an integer a ValueError will occur.
# When will a ZeroDivisionError occur?
# Answer:If the user enters 0 as a denominator a ZeroDivisionError will occur, Because a number cannot be divided by zero.
# Could you change the code to avoid the possibility of a ZeroDivisionError?
# Answer: Tried but failed unfortunately.