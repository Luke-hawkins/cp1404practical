"""
emails
Estimate: 30 minutes
Actual:   40 minutes
"""


def main():
    """Stores names and email in dictionary"""
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = check_name(email)
        email_to_name[email] = name.title()
        email = input("Email: ")
    display_emails_with_names(email_to_name)


def check_name(email):
    """Checks name at beginning of email"""
    # extracts characters before @ in email and replaces periods with spaces
    name = " ".join(email.split("@").pop(0).split(".")).title()
    choice = input(f"Is your name {name}? (Y/n) ").upper()
    if choice != "Y":
        name = input("Name: ")
    return name


def display_emails_with_names(email_to_name):
    """Displays email address with name"""
    [print(name + " : " + email_to_name[name]) for name in email_to_name]


main()
