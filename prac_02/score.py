"""
CP1404 2025 TR1 Week_2
Program 1 : Score
Student Name: Abid Hasan
Date started: 10/02/2025
"""
import random
def main():
    """Main function to get input, determine score status, and generate a random score."""
    score = float(input("Enter score: "))
    result = determine_score_status(score)
    print(result)

    # Generate a random score and determine status
    random_score = random.randint(0, 100)
    random_result = determine_score_status(random_score)
    print(f"Random score: {random_score:.2f}-- {random_result}")

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
main()
