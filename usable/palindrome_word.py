# This python code will ask the user for a word
# and the program will test if it's a palindrome

def is_palindrome(text):
    # Create a variable that will read the word backwards
    result = text[::-1]

    # If text entered matches backwards, print that it is
    # else, print that it's not
    if text.casefold() == result.casefold():
        print('')
        print(f'{text} IS a palindrome ')
    else:
        print('')
        print(f'{text} is NOT palindrome ')

    # Return the result to out of the module
    return result


# Get input from user for a word to test
text = str(input("What's a word you'd like to test? \n"))

# Call the function with the text from user
is_palindrome(text)
