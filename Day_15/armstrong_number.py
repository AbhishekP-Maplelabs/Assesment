"""
    Description: python program to check for armstrong number
"""
def armstrong_number(number):
    """
        Function to check if the given number is armstrong number or not.
    """
    length = len(str(number))
    total = 0
    while number > 0:
        digit = number % 10
        total += digit ** length
        number //= 10
    return total
if __name__ == "__main__":
    try:
        NUMBER=int(input("Enter the number"))
        TOTAL=armstrong_number(NUMBER)
        if NUMBER == TOTAL:
            print(f"{NUMBER} is an Armstrong number")
        else:
            print(f"{NUMBER} is not an Armstrong number")
    except ValueError as v:
        print("Enter valid input")
