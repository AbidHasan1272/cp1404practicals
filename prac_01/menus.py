"""
CP1404 2025 TR1 Week_1
Program 1 : Menu
Student Name: Abid Hasan
Date started: 05/02/2025
"""
name= input("Enter your name: ")
print("(H)ello")
print("(G)oodbye")
print("(Q)uit")
choice= input(">>>").capitalize()
while choice!="Q":
    if choice=="H":
        print(f"HELLO, {name}")
    elif choice=="G":
        print(f"GOODBYE {name}")
    else:
        print("Invalid choice")
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")
    choice = input(">>>").capitalize()
print("Finished")



