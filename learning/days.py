# Create a date program that pulls the current day as 'today' then count out 7 days

from datetime import date
import datetime


def week_day(day_of_week):
    if day_of_week == 0:
        return "Monday"
    elif day_of_week == 1:
        return "Tuesday"
    elif day_of_week == 2:
        return "Wednesday"
    elif day_of_week == 3:
        return "Thursday"
    elif day_of_week == 4:
        return "Friday"
    elif day_of_week == 5:
        return "Saturday"
    elif day_of_week == 6:
        return "Sunday"


def is_today(day_of_week):
    to_day = day_of_week
    if day_of_week == to_day:
        return "Today"


def print_week(today,day_of_week):
    day = date.weekday(today)

    while day < 7:
        if is_today(day) == "Today":
            print(is_today(day_of_week))
        else:
            print(week_day(day))
        day += 1


def main():
    today = date.today()
    day_of_week = week_day(int(date.weekday(today)))

    print_week(today,day_of_week)


if __name__ == '__main__':
    main()