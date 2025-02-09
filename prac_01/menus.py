from queue import PriorityQueue

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



