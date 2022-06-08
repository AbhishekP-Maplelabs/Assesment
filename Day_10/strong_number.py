"""
    Description: To find the strong number
"""
def strong_number(number):
    """
        Function to print whether the given number is strong number or not.
    """
    factorial_sum=0
    temp=number
    while number:
        i=1
        factorial=1
        rem=number%10
        while i<=rem:
            factorial=factorial*i
            i+=1
        factorial_sum=factorial_sum+factorial
        number=number//10
    if factorial_sum==temp:
        print("Given number is a strong number")
    else:
        print("Given number is not a strong number")
if __name__ == "__main__":
    try:
        NUMBER=int(input("Enter a number:"))
        strong_number(NUMBER)
    except ValueError as v:
        print("Enter valid input")
