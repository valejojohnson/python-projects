# Create a salary calculator based on an hourly input

def to_money(amount):
    new_amount = "{:,.0f}".format(int(amount))
    return new_amount


def rates(perhour):
    # Tax rates
    socsec_rate = 6.2 / 100  # Social Security tax rate
    medicare_rate = 1.45 / 100  # Medicare tax rate
    federal_tax_rate = 12 / 100  # Estimate for federal tax withholding (adjust as necessary)

    # Gross pay calculations
    daily_gross = perhour * 8
    weekly_gross = daily_gross * 5
    biweekly_gross = weekly_gross * 2
    monthly_gross = biweekly_gross * 2
    annual_gross = monthly_gross * 12

    # Tax deductions
    social_security = annual_gross * socsec_rate
    medicare = annual_gross * medicare_rate
    federal_tax = annual_gross * federal_tax_rate

    # Total deductions
    total_deductions = social_security + medicare + federal_tax

    # Net pay (take-home pay)
    annual_takehome = annual_gross - total_deductions
    monthly_takehome = annual_takehome / 12
    biweekly_takehome = monthly_takehome / 2
    weekly_takehome = biweekly_takehome / 2
    daily_takehome = weekly_takehome / 5

    print()
    print(f"The take-home rates based on ${perhour}/hr\n"
          f"Daily: ${to_money(daily_takehome)}\n"
          f"Weekly: ${to_money(weekly_takehome)}\n"
          f"BiWeekly: ${to_money(biweekly_takehome)}\n"
          f"Monthly: ${to_money(monthly_takehome)}\n"
          f"Annually: ${to_money(annual_takehome)}"
          )


def main():
    while True:
        perhour = input("How much is the hourly rate? (Enter numbers only) \n")
        if perhour.isnumeric():
            rates(float(perhour))
        else:
            rates(float(perhour))

        print()

        cont = str(input("Do you want to enter another rate? ('Y' to continue, any other key to exit)\n")).casefold()
        if cont != "y":
            print("Exiting Program. Goodbye")
            break


if __name__ == "__main__":
    main()