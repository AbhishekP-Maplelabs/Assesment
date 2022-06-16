"""
    Description: Python program to check whether
    a string starts and ends with the same character or not.
"""
import re
def check_string(string):
    """
        Function to check whether a string starts and ends with the same character or not.
    """
    regex = r'^[a-z]$|^([a-z]).*\1$'
    if re.search(regex, string):
        print("true")
    else:
        print("false")
if __name__ == '__main__' :
    try:
        STRING=input("Enter the string: ")
        check_string(STRING)
    except ValueError as v:
        print("Enter valid input")
