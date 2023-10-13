def main():
    """Displays total price after discount"""
    count = 0
    total = 0
    number_of_items = int(input("Number of items: "))
    while number_of_items < 0:
        print("Invalid number of items!")
        number_of_items = int(input("Number of items: "))
    while count != number_of_items:
        count += 1
        item_cost = float(input("Price of item: "))
        total += item_cost
    if total > 100:
        total = calculate_discount(total)
    print(f"Total price for 3 items is ${total:.2f}")


def calculate_discount(total):
    """calculates discount"""
    return total * 0.9


main()
