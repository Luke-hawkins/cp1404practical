def main():
    """randomly pick numbers of list to display"""
    import random
    NUMBER_OF_COLUMNS = 6
    count = 0
    quick_pick = []
    numbers = list(range(1, 46))
    total_quick_picks = int(input("How many quick picks? :"))
    while count != total_quick_picks:
        count += 1
        while len(quick_pick) != NUMBER_OF_COLUMNS:
            random_number = random.choice(numbers)
            while random_number in quick_pick:
                random_number = random.choice(numbers)
            quick_pick.append(random_number)
        print(quick_pick)
        # Empties quick_pick list
        quick_pick.clear()


main()
