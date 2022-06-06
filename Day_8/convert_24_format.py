"""
    Description: To convert 12 hour time format to 24 hour format
"""
def convert(time):
    """
        Function to convert 12 hour time format to 24 hour format
    """
    if time[-2:] == "AM" and time[:2] == "12":
        return "00" + time[2:-2]
    if time[-2:] == "AM":
        return time[:-2]
    if time[-2:] == "PM" and time[:2] == "12":
        return time[:-2]
    return str(int(time[:2]) + 12) + time[2:8]
if __name__ == "__main__":
    TIME="01:30:30PM"
    print("12-hour Format time:: ", TIME)
    print("24-hour Format time ::",convert(TIME))
