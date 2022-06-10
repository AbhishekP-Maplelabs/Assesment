"""
    Description: To find the time difference.
"""
from datetime import datetime
def time_difference(current_hour,current_minute,given_hour,given_minute):
    """
        Function to print the time difference between current time and given time.
    """
    hour=0
    minute=0
    if current_hour != given_hour:
        if current_hour>given_hour:
            hour=current_hour-given_hour
        else:
            hour=given_hour-current_hour
    if current_minute!=given_minute:
        if current_minute>given_minute:
            minute=current_minute-given_minute
        else:
            minute=given_minute-current_minute
    print(f"Difference in time is: {hour}:{minute}")
if __name__ == "__main__":
    try:
        NOW = datetime.now()
        CURRENT_TIME = NOW.strftime("%H:%M")
        CURRENT_HOUR=int(CURRENT_TIME[:2])
        if int(CURRENT_TIME[:2])>12:
            CURRENT_HOUR=int(CURRENT_TIME[:2])-12
        CURRENT_MINUTE=int(CURRENT_TIME[2:].replace(":",""))
        GIVEN_HOUR=int(input("Enter the hour value: "))
        GIVEN_MINUTE=int(input("Enter minute value: "))
        time_difference(CURRENT_HOUR,CURRENT_MINUTE,GIVEN_HOUR,GIVEN_MINUTE)
    except ValueError as v:
        print("Enter vlid time value")
