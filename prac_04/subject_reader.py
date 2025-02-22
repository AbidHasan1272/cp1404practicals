"""
CP1404/CP5632 Practical
Program: Data file -> lists program
Student Name:Abid Hasan
Date:22/02/2025
"""
FILENAME = "subject_data.txt"

def main():
    subjects = load_data()
    display_subject_details(subjects)

def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    with open(FILENAME, 'r') as file:
        for line in file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            data.append(parts)
    return data

def display_subject_details(subjects):
    """Display subject details in a formatted manner."""
    for subject in subjects:  # Loop through each subject in the list
        print(f"{subject[0]} is taught by {subject[1]:12} and has {subject[2]:35} students")

main()
