# This code is to work on removing a letter from a
# sentence and recreate the sentence without that
# letter.


def remove_letter(quote, to_remove):
    new_sentence = ''
    # Go through every letter in the quote
    for char in quote:
        # If a letter in the to_remove variable is found, don't add it to new sentence
        if char != to_remove:
            new_sentence = new_sentence + char
    # Return the new sentence back without letter from to_remove variable
    return new_sentence


def too_long(quote):
    # This function is to test if the quote entered
    # was greater than 50 characters

    while len(quote) > 50:
        print("EEK, that's a long sentence!")
        quote = input("Type in a shorter sentence: ").strip()
    return quote


def main():
    quote = input("Type in a sentence you'd like to test with: ").strip()
    quote = too_long(quote)

    to_remove = input("What's the letter you'd like to remove? ").strip()
    print(remove_letter(quote, to_remove))


if __name__ == '__main__':
    main()
