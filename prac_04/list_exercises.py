def main():
    """gets 5 numbers from user to display summary"""
    NUMBER_OF_NUMBERS = 5
    count = 0
    numbers = []
    while count != NUMBER_OF_NUMBERS:
        count += 1
        number = int(input(f"Number {count}: "))
        numbers.append(number)
    numbers_summary(numbers)


def numbers_summary(numbers):
    """prints summary of numbers"""
    from statistics import mean
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {mean(numbers)}")


main()
