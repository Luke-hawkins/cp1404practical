"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    summarize_data(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects_information = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)
        # See if that worked
        subjects_information.append(parts)
        print("----------")
    input_file.close()
    return subjects_information


def summarize_data(data):
    """summarizes data for each subject"""
    for subjects in data:
        print(f"{subjects[0]} is taught by {subjects[1]} and has {subjects[2]} students")


main()
