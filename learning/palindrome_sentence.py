def is_palindrome(sentence):
    # Will need to create a new sentence as we want to ignore non-alphanumeric characters
    new_sentence = ''

    # This is to go through each character and create the new sentence if character is not alphanumeric
    for char in sentence:
        if char.isalnum():
            new_sentence = new_sentence + char

    # Result should be newly created sentence backwards
    result = new_sentence[::-1]

    if new_sentence.casefold() == result.casefold():
        print("Sentence is Palindrome")
    else:
        print("Sentence is NOT palindrome")


sentence = input("What sentence would you like to test? ")
is_palindrome(sentence)
