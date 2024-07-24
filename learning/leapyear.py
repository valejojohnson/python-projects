#year = input("Input a year to test: e.g (YYYY) \n")

year = 2024


def isleap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")


isleap(year)
