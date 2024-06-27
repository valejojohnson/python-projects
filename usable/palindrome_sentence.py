# This python code is designed to test if a sentence
# is a palindrome or not

# Function to generate a new sentence based on input
# by removing all but letters, then testing if it matches
# as palindrome
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
        print(f"The sentence {sentence} IS Palindrome")
    else:
        print(f"The sentence {sentence} is NOT palindrome")


# Taking input from user no matter the case or characters used
sentence = input("What sentence would you like to test? ")
is_palindrome(sentence)


# Sentences to test
# Do Geese See God?
# Was it a car or a cat I saw?
# Mr. Owl ate my metal worm