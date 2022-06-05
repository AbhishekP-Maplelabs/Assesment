"""
    Description: To print the words which have the size as specified by user
"""
import sys
def word_length(number):
    """
        This function will print those words which has the length given by the user
    """
    string_list=[]
    string_list=[]
    for word in range(number):
        word=input()
        if word.isnumeric():
            print("Enter proper word")
            sys.exit()
        else:
            string_list.append(word)
    print(f"Original list: {string_list}")
    string_length=int(input("Enter the length of string to extract"))
    for string in string_list:
        if len(string)==string_length:
            string_list.append(string)
    print(f"After extracting strings of specified length from the said list: {string_list}")
try:
    NUMBER=int(input("Enter the number of words in the list: "))
    word_length(NUMBER)
except Exception as e:
    print("Enter the valid input")
