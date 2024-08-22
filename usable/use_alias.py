# This code is to use an alias name if present
# if no alias, just use regular first name


def get_input(prompt):
    return input(prompt).strip().capitalize()


def main():
    first_name = get_input("What's your first name? \n")
    print()

    last_name = get_input(f"Hi {first_name}, what's your last name? \n")
    print()

    alias = get_input("Do you have a nickname you like to be called? (Press Enter to Skip) \n")
    print()

    if not alias or alias == 'no'.casefold():
        print(f"Hi {first_name} {last_name}. We're happy to have you here")
    else:
        print(f"Hi {alias} {last_name}. We're happy to have you here")


if __name__ == "__main__":
    main()
