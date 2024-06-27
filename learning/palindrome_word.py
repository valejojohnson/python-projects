def is_palindrome(text):
    result = text[::-1]
    if text.lower() == result.lower():
        print('')
        print(f'{text} IS a palindrome ')
    else:
        print('')
        print(f'{text} is NOT palindrome ')

    return result


text = str(input("What's a word you'd like to test? "))
is_palindrome(text)
