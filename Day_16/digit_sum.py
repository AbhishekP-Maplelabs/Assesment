"""
    Description: Python program to find the sum of even and odd digits fron given number
"""
def odd_even_sum(input_number):
    """
        Function to print the sum of even and odd digits from given number.
    """
    even_sum=0
    odd_sum=0
    for number in str(input_number):
        digit=int(number)
        if digit % 2 == 0:
            even_sum+=digit
        else:
            odd_sum+=digit
    difference=odd_sum-even_sum
    return difference
if __name__ == "__main__":
    try:
        NUMBER=int(input("Enter the number"))
        DIFFERENCE=odd_even_sum(NUMBER)
        print(f"The difference between the sum of odd digts and even digits is: {DIFFERENCE}")
    except ValueError as v:
        print("Enter valid input")
