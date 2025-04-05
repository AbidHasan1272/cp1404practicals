"""
CP1404/CP5632 Practical
Program:- Guitar class
Name:Abid Hasan
Estimate: 15 minutes
Actual:   10  minutes
"""
CURRENT_YEAR = 2025  # Update this each year if needed

class Guitar:
    """Represents a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string representation guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more.
        if not then False."""
        return self.get_age() >= 50
