"""
    To find the number of ways the train stops at given stops between given intermediate stations
    such that no two stops are consicative.
"""
def stopping_station( stations, stops):
    """
    this function takes number of stations and number of stops as input and
    calculates the number of ways that a train stops at given stops between given
    intermediate stationssuch that no two stops are consicative.
    """
    num = 1
    dem = 1
    ways = stops
    while stops != 1:
        dem *= stops
        stops-=1
    temp = stations - ways + 1
    while temp != (stations-2 * ways + 1):
        num *= temp
        temp-=1
    if (stations - ways + 1) >= ways:
        return int(num/dem)
    return -1
if __name__=="__main__":
    try:
        STATIONS=int(input("Enter the number of stations: "))
        STOPS=int(input("Enter the number of stops: "))
        NUM = stopping_station(STATIONS, STOPS)
        if NUM != -1:
            print(f"The number of ways train stops is: {NUM}")
        else:
            print("Not Possible")
    except Exception as e:
        print("Enter valid input")
