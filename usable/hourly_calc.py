# Create a salary calculator based on an hourly input

def rates(perhour):
    amount = perhour
    day = amount * 8
    week = day * 5
    biweekly = week * 2
    monthly = biweekly * 2
    annually = monthly * 12
    print()
    print(f"The rates based on ${amount} per-hour\n"
          f"Daily: ${day}\n"
          f"Weekly: ${week}\n"
          f"BiWeekly: ${biweekly}\n"
          f"Monthly: ${monthly}\n"
          f"Annually: ${annually}"
          )


def main():
    while True:
        perhour = int(input("How much is the hourly rate? (Enter numbers only) \n"))
        rates(perhour)
        print()
        cont = str(input("Do you want to enter another rate? ('Y' to continue, any other key to exit)\n")).casefold()
        if cont != "y":
            print("Exiting Program. Goodbye")
            break


if __name__ == "__main__":
    main()