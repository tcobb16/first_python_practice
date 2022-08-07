def print_upper_words(words):
    """Prints each word on its own line and fully uppercased"""

    for word in words:
        print(word.upper())


def print_upper_words_e(words):
    """Prints only words starting with e, still on their own line and uppercased"""

    for word in words:
        if word.startswith("E") or word.startswith("e"):
            print (word.upper())


def print_upper_words_gen(words, must_start_with):
    """Prints each word in uppercase on its own line as long as it starts with the specified letter that's passed in"""

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break