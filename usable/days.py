from datetime import date, timedelta


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


def is_today(day, today):
    return day == today


def print_week(today):
    day = today.weekday()

    for i in range(7):
        current_day = (day + i) % 7
        if is_today(current_day, day):
            print("Today")
        else:
            print(week_day(current_day))


def main():
    today = date.today()
    print_week(today)

if __name__ == '__main__':
    main()