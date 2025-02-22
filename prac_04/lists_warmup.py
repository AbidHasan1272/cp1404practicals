numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0]=3
# numbers[-1]=2
# numbers[3]=1
# numbers[:-1]=[3,1,4,1,5,9,2]
# numbers[3:4]=[1]
# 5 in numbers=False
# 7 in numbers=False
# "3" in numbers=False
# numbers + [6, 5, 3]=[3, 1, 4, 1, 5, 9, 2,6, 5, 3]

"""Checked all the answers in the python console all of them were right
"""

# Part_2

# Change the first element of numbers to "ten"
numbers[0]="ten"

# Change the last element of numbers to 1
numbers[-1]=1

# Print all the elements from numbers except the first two (slice)
print(numbers[2:])

# Print whether 9 is an element of numbers
if 9 in numbers:
    print("Yes, 9 is in the list ")
else:
    print("Nope,no trace of 9 here")

