# This code is to use an alias name if present
# if no alias, just use regular name


def get_input(prompt):
    return input(prompt).strip().capitalize()


first_name = get_input("What's your first name? ")
print()

last_name = get_input(f"Hi {first_name}, what's your last name? ")
print()

alias = get_input("Do you have a nickname you like to be called? ")
print()

if not alias:
    print(f"Hi {first_name} {last_name}. We're happy to have you here")
else:
    print(f"Hi {alias} {last_name}. We're happy to have you here")
