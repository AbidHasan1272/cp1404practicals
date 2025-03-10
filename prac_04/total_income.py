"""
CP1404/CP5632 Practical
Program: Total income program
Student Name:Abid Hasan
Date:22/02/2025

"""
def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))
    get_monthly_earnings(incomes, number_of_months)
    print_report(incomes, number_of_months)


def get_monthly_earnings(incomes, number_of_months):
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {str(month)} : "))
        incomes.append(income)


def print_report(incomes, number_of_months):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()