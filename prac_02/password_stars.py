"""
CP1404 2025 TR1 Week_2
Program 1 : Password Stars
Student Name: Abid Hasan
Date started: 14/02/2025
"""
MIN= 10
def main():
    enter_pass = get_password()
    print_asterisks(enter_pass)

def get_password():
    """Takes user input & keeps asking until they enter valid length of characters as password"""
    enter_pass = input("Enter password:")
    while len(enter_pass) < MIN:
        print("Invalid Password")
        enter_pass = input("Enter password:")
    return enter_pass

def print_asterisks(enter_pass):
    """Print asterisks equivalent to the password length."""
    print("*" * len(enter_pass))
main()


