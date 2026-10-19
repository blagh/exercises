from datetime import date, datetime


def get_sundays(year, month):
    first_date = date(year, month, 1)

    # sunday is 6
    # monday: 1 + (6 - 0) (7th)
    # tuesday: 1 + (6 - 1) (6th)
    # ..
    # saturday: 1 + (6 - 5) (2nd)
    # sunday: 1 + (6 - 6) (1st)
    weekday_of_first = datetime.weekday(first_date)
    days_to_sunday = 6 - weekday_of_first

    first_sunday_date = date(year, month, 1 + days_to_sunday)

    sundays = [first_sunday_date]
    next_sunday = first_sunday_date
    try:
        while True:
            next_sunday = date(year, month, next_sunday.day + 7)
            sundays.append(next_sunday) 
    except ValueError:
        pass

    return [s.isoformat() for s in sundays]

print(get_sundays(2026, 9))

print(get_sundays(2023, 9))

