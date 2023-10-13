"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """displays result based on score"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)
    score = random.randint(0, 100)
    result = determine_result(score)
    print(f"with a random score of {score} the result is : {result}")


def determine_result(score):
    """determine_results based on score"""
    if score > 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
