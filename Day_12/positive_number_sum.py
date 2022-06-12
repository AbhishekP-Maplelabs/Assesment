"""
    Description: To add the number entered until the user enters negative number.
"""
def number_sum(num_range):
    """
        Function to add the positive numbers till user enters negative number
    """
    addition=0
    for num in range(num_range):
        num=int(input())
        if num < 0:
            break
        addition=addition+num
    return addition
if __name__ == "__main__":
    try:
        NUM_RANGE=int(input("Enter the range of numbers "))
        ADDITION=number_sum(NUM_RANGE)
        print(f"the sum of positive numbers  is: {ADDITION}")
    except ValueError as v:
        print("Enter valid input")
