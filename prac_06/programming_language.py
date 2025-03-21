"""CP1404/CP5632 Practical
Program:- ProgrammingLanguage Class
Name:Abid Hasan
Estimate: 15 minutes
Actual:   17 minutes
"""
class ProgrammingLanguage:
    """Represent a Programming Language object."""

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection},First appeared in {self.year}"

    def is_dynamic(self):
        """Return True if language is dynamically typed."""
        return self.typing.lower() == "dynamic"