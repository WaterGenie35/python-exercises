from datetime import date, timedelta


def solution():
    """
    Solution to Project Euler problem 19
    https://projecteuler.net/problem=19

    Find the number of Sundays that are also the 1st day of the month in the
    twentieth century (1901-01-01 to 2000-12-31).

    Assume:
        - 1900-01-01 is Monday
        - Month 2 has 28 days on non-leap years, 29 days on leap years
        - Month 4, 6, 9, and 11 have 30 days
        - All other months have 31 days
        - A year is a leap year if [it is divisible by 400] or [it is divisible
          by 4 and not by 100]
    """
    print(num_sundays_first_of_month(date(1901, 1, 1), date(2000, 12, 31)))


def test_solution():
    assert num_sundays_first_of_month(date(1901, 1, 1), date(2000, 12, 31)) == 171


def num_sundays_first_of_month(start_date: date, end_date: date) -> int:
    num = 0
    head = start_date
    while head <= end_date:
        if head.day == 1 and is_sunday(head):
            num += 1
        head += timedelta(days=1)
    return num


def is_sunday(d: date) -> bool:
    return d.weekday() == 6
