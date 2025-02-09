"""
CP1404/CP5632 - Practical
4 consecutive loops
"""
# A.count in 10s from 0 to 100
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# B.count down from 20 to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# C.print n stars. Ask the user for a number, then print that many stars (*), all on one line
number_of_stars =int (input("Enter the number of stars : "))
print("*"* number_of_stars)

# D. print n lines of increasing stars. Using the same number as above, print lines of increasing stars, starting at 1 with no blank line.

number_of_stars =int (input("Enter the number of stars : "))
for i in range(1, number_of_stars + 1):
    print("*" * i)