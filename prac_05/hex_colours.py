def main():
    """displays Hex code based of users colour input"""
    colour_to_hex = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a",
                     "Alizarin crimson": "#e32636", "Amaranth": "#e52b50",
                     "Amber": "#ffbf00", "Amethyst": "#9966cc",
                     "AntiqueWhite": "#faebd7", "Azure3": "#c1cdcd",
                     "Azure4": "#838b8b", "Baby Blue": "#89cff0",
                     "Baby Pink": "#f4c2c2", "Baker-Miller Pink": "#ff91af",
                     "Banana Mania": "#fae7b5", "Banana Yellow": "#ffe135",
                     "Barn Red": "#7c0a02", "Battleship Gray": "#848482"}

    colour = input("colour: ").title()
    while colour != "":
        try:
            print(colour, "hexadecimal colour code: ", colour_to_hex[colour])
        except KeyError:
            print("no")
        colour = input("colour: ").title()


main()
