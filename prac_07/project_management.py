"""
CP1404/CP5632 Practical
Project Management System
Estimate: 60 minutes
Actual: (fill this in after testing)
"""

from project import Project

FILENAME = "projects.txt"


def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(FILENAME)
    print(f"Loaded {len(projects)} projects from {FILENAME}")

    menu = "\n- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n" \
           "- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit"

    print(menu)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            filename = input("Filename: ")
            projects = load_projects(filename)
        elif choice == "s":
            filename = input("Filename: ")
            save_projects(filename, projects)
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            filter_projects_by_date(projects)
        elif choice == "a":
            add_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid menu choice.")
        print(menu)
        choice = input(">>> ").lower()

    save_decision = input("Would you like to save to projects.txt? ").lower()
    if save_decision in ['yes', 'y']:
        save_projects(FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from file."""
    projects = []
    with open(filename, 'r') as file:
        file.readline()  # Skip header
        for line in file:
            parts = line.strip().split('\t')
            projects.append(Project(*parts))
    return projects


def save_projects(filename, projects):
    """Save all projects to a file."""
    with open(filename, 'w') as file:
        file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.cost_estimate}\t{project.percent_complete}\n")


def display_projects(projects):
    """Display incomplete and completed projects sorted by priority."""
    incomplete = [p for p in projects if not p.is_complete()]
    complete = [p for p in projects if p.is_complete()]

    print("Incomplete projects:")
    for p in sorted(incomplete):
        print(f"  {p}")
    print("Completed projects:")
    for p in sorted(complete):
        print(f"  {p}")


def filter_projects_by_date(projects):
    """Filter and display projects starting after a given date."""
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.strptime(date_str, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date format.")
        return
    filtered = [p for p in projects if p.start_date > filter_date]
    for p in sorted(filtered, key=lambda proj: proj.start_date):
        print(p)


def add_project(projects):
    """Add a new project to the list."""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost = input("Cost estimate: $")
    completion = input("Percent complete: ")
    projects.append(Project(name, start_date, priority, cost, completion))


def update_project(projects):
    """Update a selected project's completion and/or priority."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    try:
        index = int(input("Project choice: "))
        project = projects[index]
        print(project)
        new_percent = input("New Percentage: ")
        new_priority = input("New Priority: ")
        project.update(new_percent, new_priority)
    except (ValueError, IndexError):
        print("Invalid selection.")


main()
