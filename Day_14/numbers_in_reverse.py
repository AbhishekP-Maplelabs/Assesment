"""
    Description:To print the natural numbers in reverse order
"""
def reverse_order(num_range):
    """
        Function to print natural numbers in reverse order
    """
    for num in range(num_range,0,-1):
        print(num,end=" ")
if __name__ == "__main__":
    try:
        RANGE=int(input("Enter the range of number: "))
        reverse_order(RANGE)
    except ValueError as v:
        print("Enter valid input")
    except TypeError as t:
        print("Provide proper values")
