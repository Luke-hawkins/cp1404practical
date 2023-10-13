def main():
    """sore password"""
    password = get_password()
    PASSWORD_MIN_LENGTH = 0
    while len(password) <= PASSWORD_MIN_LENGTH:
        password = get_password()
    print_asterisks(password)


def get_password():
    """get password"""
    password = input("Password: ")
    return password


def print_asterisks(password):
    """print string of asterisks the length of password"""
    print(len(password) * "*")


main()
