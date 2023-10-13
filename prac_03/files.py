def main():
    OUTPUT_FILE_FOR_NAME = "name.txt"
    OUTPUT_FILE_FOR_NUMBERS = "numbers.txt"
    question_1(OUTPUT_FILE_FOR_NAME)
    question_2(OUTPUT_FILE_FOR_NAME)
    question_3(OUTPUT_FILE_FOR_NUMBERS)
    question_4(OUTPUT_FILE_FOR_NUMBERS)


def question_1(OUTPUT_FILE_FOR_NAME):
    name = input("Name: ")
    out_file = open(OUTPUT_FILE_FOR_NAME, 'w')
    print(name, file=out_file)
    out_file.close()


def question_2(OUTPUT_FILE_FOR_NAME):
    out_file = open(OUTPUT_FILE_FOR_NAME, 'r')
    for line in out_file:
        print(f"Your name is {line.title()}")
    out_file.close()


def question_3(OUTPUT_FILE_FOR_NUMBERS):
    total = 0
    out_file = open(OUTPUT_FILE_FOR_NUMBERS, 'r')
    total += int(out_file.readline())
    total += int(out_file.readline())
    out_file.close()
    print(f"The total of the first 2 lines is {total}")


def question_4(OUTPUT_FILE_FOR_NUMBERS):
    total = 0
    out_file = open(OUTPUT_FILE_FOR_NUMBERS, 'r')
    for line in out_file:
        total += int(line)
    print(f"the total of all lines is {total}")


main()
