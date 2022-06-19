"""
module:1
description:To find the sum of items in the dictionary
"""
def return_sum(my_dict):
    """
    finds the sum of items in the dictionary
    """
    value_list = list(my_dict.values())
    return sum(value_list)
try:
    NUMBER = int(input("Enter the length od dictionary: "))
    my_Dictionary = {}
    for x in range(NUMBER):
        input_dict = input("Enter key and value:").split(":")
        my_Dictionary[input_dict[0]] = int(input_dict[1])
    TOTAL=return_sum(my_Dictionary)
    print(f"The sum of items in dictionary is: {TOTAL}")
except ValueError as v:
    print("Enter the valid input")
