"""
description: To find the next date based on the date user has given
"""
def next_date(year,month,day):
    """
    This function will print the next date of which the user has entered
    """
    if year % 400 == 0:
        leap_year = True
    elif year % 100 == 0:
        leap_year = False
    elif year % 4 == 0:
        leap_year = True
    else:
        leap_year = False
    if month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif month == 2:
        if leap_year:
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30
    if day < month_length:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    print(f"The next date is [yyyy-mm-dd] %d-%d-%d {year, month, day}")
try:
    YEAR = int(input("Input a year: "))
    MONTH = int(input("Input a month [1-12]: "))
    if MONTH>12:
        print("Enter valid month")
    else:
        DAY = int(input("Input a day [1-31]: "))
        if DAY>31:
            print("Enter the valid day")
        else:
            next_date(YEAR,MONTH,DAY)
except Exception as e:
    print("Enter the valid inputs")
