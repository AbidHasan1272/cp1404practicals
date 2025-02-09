"""
CP1404/CP5632 - Practical
Code for temperature conversion
"""
def main():
    """Display menu and handle user choice for temperature conversion."""
    menu = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
    print(menu)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")

        print(menu)
        choice = input(">>> ").upper()

    print("Thank you.")

def celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return celsius * 9 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return 5 / 9 * (fahrenheit - 32)

main()

