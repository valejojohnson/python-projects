# Create a program that places a comma three digits in (Like a currency)

def third_comma(amount):
    new_amount = "${:,.0f}".format(int(amount))
    return new_amount

def main():
    while True:
        amount = input("Give me a number:\n")
        print(third_comma(amount))

        print()

        again = str(input("Do you want to input another number? ('Y' for Yes, Any other key to quit)\n"))
        if again != 'y'.casefold():
            break


if __name__ == '__main__':
    main()