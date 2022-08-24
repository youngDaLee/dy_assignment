MONTH_DAY = {
    1 : 31,
    2 : 28,
    3 : 31,
    4 : 30,
    5 : 31,
    6 : 30,
    7 : 31,
    8 : 31,
    9 : 30,
    10 : 31,
    11 : 30,
    12 : 31,
}


def add_leap(year, month):
    """Get leap_year's febuary days
    Sample usage:
    >>> add_leap(1900, 2)
    0
    >>> add_leap(2000, 1)
    0
    >>> add_leap(2000, 2)
    1
    """
    if (month == 2) and ((year%4==0 and year%100 !=0) or (year%400==0)):
        print(year, month)
        return 1
    else:
        return 0


def get_fisrt_sunday():
    """Get Sundays fell on the first of the month during 1901-01-01 to 2000-12-31
    Sample usage:
    >>> get_first_sunday
    """
    year = 1900
    month = 2
    day = 0
    monday_cnt = 1

    # Add the Days Until Divisible by 7
    while year < 2001:
        day += MONTH_DAY[month] + add_leap(year, month)
        if day % 7 == 0:
            monday_cnt += 1
            day = 0

        if month == 12:
            month = 1
            year += 1
        else:
            month += 1 

    return monday_cnt


if __name__ == '__main__':
    print(get_fisrt_sunday())
