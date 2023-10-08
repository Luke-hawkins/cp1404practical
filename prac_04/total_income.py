"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    total_months = int(input("How many months? "))

    for total_months in range(1, total_months + 1):
        income = float(input(f"Enter income for month {total_months} : "))
        incomes.append(income)

    print_income_report(total_months, incomes)


def print_income_report(total_months, incomes):
    """display income report"""
    print("\nIncome Report\n-------------")
    total = 0
    for total_months in range(1, total_months + 1):
        income = incomes[total_months - 1]
        total += income
        print(f"Month {total_months} - Income: ${income:.f2} Total: ${total:.2f}")


main()
