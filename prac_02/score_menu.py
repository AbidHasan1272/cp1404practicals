"""
CP1404 2025 TR1 Week_2
Program 1 : Score Menu
Student Name: Abid Hasan
Date started: 10/02/2025
"""
def main():
    """Display menu and handle user choice for temperature conversion."""
    score = get_valid_score()
    menu = """G - Get a valid score(0-100)
P - Print result
S - Show stars
Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice =="G":
            get_valid_score()
        elif choice =="P":
            print(determine_score_status(score))
        elif choice =="S":
            print_asterisks(score)
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Farewell")

def get_valid_score():
    score =int (input("Enter score(0-100):"))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score(0-100):"))
    return score

def determine_score_status(score):
    """Determine the status of score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"

def print_asterisks(score):
    """Print asterisks equivalent to the score length."""
    print("*" * score)

main()