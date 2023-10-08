"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""


def main():
    """Display bonus"""
    sales = float(input("Enter sales: $"))
    LOW_BONUS_PERCENT = 0.1
    HIGH_BONUS_PERCENT = 0.15
    while sales >= 0:
        bonus = calculate_bonus(sales, LOW_BONUS_PERCENT, HIGH_BONUS_PERCENT)
        print(f"Bonus: ${bonus:.2f}")
        sales = float(input("Enter sales: $"))
    print("Done...")


def calculate_bonus(sales, LOW_BONUS_PERCENT, HIGH_BONUS_PERCENT):
    """calculate bonus based of sales"""
    if sales < 1000:
        return sales * LOW_BONUS_PERCENT
    else:
        return sales * HIGH_BONUS_PERCENT


main()
