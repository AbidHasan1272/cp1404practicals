"""
CP1404/CP5632 Practical
Read, sort, update and save guitar data
"""

from guitar import Guitar

FILENAME = "guitar.csv"

def main():
    """Main function to manage guitars."""
    guitars = load_guitars(FILENAME)
    print("These are my guitars:")
    display_guitars(guitars)

    add_new_guitars(guitars)

    # Sort by year and display again
    guitars.sort()
    print("\nThese are my guitars (sorted by year):")
    display_guitars(guitars)

    # Save updated guitars back to file
    save_guitars(FILENAME, guitars)

def load_guitars(filename):
    """Load guitars from a CSV file into a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as in_file:
        for line in in_file:
            parts = line.strip().split(',')
            name = parts[0]
            year = int(parts[1])
            cost = float(parts[2])
            guitars.append(Guitar(name, year, cost))
    return guitars

def display_guitars(guitars):
    """Display a list of guitars with vintage status."""
    for i, guitar in enumerate(guitars, 1):
        vintage = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>30} ({guitar.year}), worth ${guitar.cost:12,.2f}{vintage}")

def add_new_guitars(guitars):
    """Prompt user to add new guitars."""
    print("\nAdd new guitars (press Enter to stop):")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.")
        name = input("Name: ")

def save_guitars(filename, guitars):
    """Save all guitars to a CSV file."""
    with open(filename, 'w') as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)

main()
