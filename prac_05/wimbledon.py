"""
wimbledon
Estimate: 30 minutes
Actual:   60 minutes
"""
import csv


def main():
    """extracts data from wimbledon.csv to display summary"""
    champion_to_wins = {}
    countries = []
    FILE_NAME = "wimbledon.csv"
    read_data(FILE_NAME, champion_to_wins, countries)
    print_champion_wins(champion_to_wins)
    print_winning_countries(countries)


def read_data(FILE_NAME, champion_to_wins, countries):
    """extracts data from wimbledon.csv and stores it in a list"""
    with open(FILE_NAME, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        for line in reader:
            champion = line[2]
            country = line[1]
            champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
            countries.append(country)
        in_file.close()


def print_champion_wins(champion_to_wins):
    """print past champions with total wins"""
    [print(champion + " : " + str(champion_to_wins[champion])) for champion in champion_to_wins]


def print_winning_countries(countries):
    """print list of countries that won wimbledon"""
    countries = list(dict.fromkeys(countries))
    print(*(country for country in sorted(countries)), sep=" ")


main()
