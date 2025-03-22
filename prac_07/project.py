"""
CP1404/CP5632 Practical
Program: Project class
Estimate: 20 Minutes
Actual: 25 Minutes
"""

from datetime import datetime

class Project:
    """Class to represent a project with relevant attributes."""

    def __init__(self, name, start_date, priority, cost_estimate, percent_complete):
        self.name = name
        self.start_date = datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.percent_complete = int(percent_complete)

    def __str__(self):
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.percent_complete}%")

    def __lt__(self, other):
        """Allows sorting projects by priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if project is 100% complete."""
        return self.percent_complete == 100

    def update(self, new_percent=None, new_priority=None):
        """Update percent complete and/or priority."""
        if new_percent != "":
            self.percent_complete = int(new_percent)
        if new_priority != "":
            self.priority = int(new_priority)
