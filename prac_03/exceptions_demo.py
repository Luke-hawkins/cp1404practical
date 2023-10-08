"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?

A value error occurs when the used value does not fit within the parameters of the function
such as finding a square root of a negative number.

2. When will a ZeroDivisionError occur?

when a number is divided by zero

3. Could you change the code to avoid the possibility of a ZeroDivisionError?

Yes, you could error check to make sure the input for the denominator is not zero
"""


def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = get_denominator()
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")


def get_denominator():
    """return users denominator"""
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero!")
        denominator = int(input("Enter the denominator: "))
    return denominator


main()
