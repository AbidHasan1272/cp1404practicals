"""
CP1404/CP5632 Practical - Client code to use the Car class.
Note that the import has a folder (module) in it.
This is why we name our folders with no spaces or capitals, as valid module names.
"""

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    limo = Car("Limo", 100)  # Create new Car with 100 fuel
    limo.add_fuel(20)  # Add 20 fuel
    print(f"Limo has fuel: {limo.fuel}")  # Print fuel amount
    limo.drive(115)  # Try to drive 115 km
    print(limo)

main()
