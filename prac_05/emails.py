"""
Emails
Estimate: 15 minutes
Actual:   30 minutes
"""

def main():
    email_to_name = {}
    get_user_email(email_to_name)
    print_output(email_to_name)


def get_user_email(email_to_name):
    "'""gets the user email and name, and checks the name with the user"""
    email = input("Email: ").strip()
    while email != "":
        name = extract_name_from_email(email)
        user_name = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if user_name == '' or user_name == 'y':
            email_to_name[email] = name
        else:
            correct_name = input("Name: ").strip()
            email_to_name[email] = correct_name
        email = input("Email: ").strip()

def extract_name_from_email(email):
    """
    Extracts the name from the email
    """
    name_part = email.split('@')[0]
    name = name_part.replace('.', ' ').replace('_', ' ').title()
    return name

def print_output(email_to_name):
    """when user enters blank email, program prints all the name and emails"""
    print("\nStored Emails and Names:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

main()
