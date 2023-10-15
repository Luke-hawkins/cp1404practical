"""
Word Occurrences
Estimate: 30 minutes
Actual:   15 minutes
"""


def main():
    """counts the occurrences of each word in a string"""
    word_to_count = {}
    text = input("Text: ").split()
    for word in text:
        if word in word_to_count:
            word_to_count[word] = word_to_count[word] + 1
        else:
            word_to_count[word] = 1

    print_word_count(word_to_count)


def print_word_count(word_to_count):
    """Displays sorted word occurrences"""
    # Finds length of the longest word in word_to_count
    width = max(map(len, word_to_count))
    [print(f"{word:{width}} : " + str(word_to_count[word])) for word in sorted(word_to_count)]


main()
