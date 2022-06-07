"""
    Description : To print the number series without using loop
"""
def print_number(num_range, original, difference, temp):
    """
        Function to print the number seris through given range
    """
    print(num_range, end = " ")
    if num_range <= 0:
        if temp==0:
            temp = 1
        else:
            temp = 0
    if num_range == original and not temp:
        return
    if temp is True:
        print_number(num_range - difference, original, difference, temp)
        return
    if not temp:
        print_number(num_range + difference, original, difference, temp)
    return
if __name__ == "__main__":
    try:
        RANGE = int(input("Enter the range of the number: "))
        DIFFERENCE = int(input("ENter the difference: "))
        print_number(RANGE, RANGE, DIFFERENCE, True)
    except ValueError as v:
        print("Enter the valid input")
