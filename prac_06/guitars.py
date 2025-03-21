"""
CP1404/CP5632 Practical
Program:- Guitar collection program
Name:Abid Hasan
Estimate: 15 minutes
Actual:   10  minutes
"""

from guitar import Guitar
def main():
    print("Collection of My guitars!")
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")

    print("\nThese are my guitars:")
    # Display all the entered guitars
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")

main()
