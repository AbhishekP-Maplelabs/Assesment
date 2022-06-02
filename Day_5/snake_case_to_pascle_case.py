"""
module:1
description:to convert snake case to pascle case
"""
from string import capwords
def convert_case(string):
    """
        Convert snake_case to PascalCase
    """
    print('In Snake Case: ',string)
    result = capwords(string.replace('_',' ')).replace(' ','')
    return result
if __name__=="__main__":
    try:
        STRING = input("Enter string in snake case: ")
        RESULT=convert_case(STRING)
        print(f"In Pascal Case: {RESULT}")
    except Exception as e:
        print("Enter valid input")
