def main():
    """get menu choice to determine result"""
    menu = "(G)et a valid score \n" \
           "(P)rint result\n" \
           "(S)how stars  \n" \
           "(Q)uit \n" \
           ">>> "
    choice = input(menu).upper()
    score = 0
    while choice != "Q":
        if choice == "G":
            score = int(input("Score: "))
            while score < 0 or score > 100:
                print("Invalid score")
                score = int(input("Score: "))
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            print_asterisk(score)
        else:
            print("invalid choice")
        choice = input(menu).upper()
    print("Some fair well")


def determine_result(score):
    """return result based on score"""
    """determine_results based on score"""
    if score > 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_asterisk(score):
    """print asterisk based on score"""
    print(score * "*")


main()
