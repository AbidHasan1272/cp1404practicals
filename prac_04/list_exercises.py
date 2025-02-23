"""
CP1404/CP5632 Practical
Program: List Exercises
Student Name:Abid Hasan
Date:22/02/2025
"""
numbers =[]
NUMBER_COUNT=5
for i in range(NUMBER_COUNT):
    number=int(input(f"Enter number {i+1}: " ))
    numbers.append(number)

total=sum(numbers)
print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The highest number is {max(numbers)}")
print(f"The average of all this number is {total/len(numbers)}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username=input("Enter Your username:")
if username in usernames:
    print("Access Granted, Welcome Mate.")
else:
    print("Access Denied, Sorry mate")