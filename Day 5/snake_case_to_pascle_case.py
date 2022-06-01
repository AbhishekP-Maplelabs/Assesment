"""
module:1
description:to convert snake case to pascle case
"""
from string import capwords
try:
    string = input("Enter string in snake case: ")
    print('In Snake Case: ',string)
    result = capwords(string.replace('_',' '))
    result = result.replace(' ','')
    print('In Pascal Case: ',result)
except Exception as e:
    print("Enter the valid input")
    