"""
    Description: To print the sum of even factors of the number
"""
import math
def even_factors_sum(number):
    """
        Function to print the sum of even factors of the given number
    """
    if number % 2 != 0 :
        return 0
    res = 1
    for i in range(2, (int)(math.sqrt(number)) + 1) :
        count = 0
        factor_sum = 1
        curr_term = 1
        while number % i == 0 :
            count= count + 1
            number = number // i
            if (i == 2 and count == 1) :
                factor_sum = 0
            curr_term = curr_term * i
            factor_sum = factor_sum + curr_term
        res = res * factor_sum
    if number >= 2 :
        res = res * (1 + number)
    return res
if __name__ == "__main__":
    try:
        NUMBER = int(input("Enter the number: "))
        print(even_factors_sum(NUMBER))
    except ValueError as v:
        print("Enter valid input")
