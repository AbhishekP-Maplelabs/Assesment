"""
    Description: To print the distinct words from the list given by the user
"""
import sys
def unique(list1):
    """
        This function will prints the unique words out of the list given by the user
    """
    unique_list = []
    for word in list1:
        if word not in unique_list:
            unique_list.append(word)
    print(len(unique_list))
    for i in range(0,len(unique_list)):
        print(f"{unique_list[i]} :1")
try:
    NUMBER=int(input("Input number of words: "))
    LIST=[]
    for WORD in range(NUMBER):
        WORD=input()
        if WORD.isnumeric():
            print("Input the words: ")
            sys.exit()
        else:
            LIST.append(WORD)
    unique(LIST)
except Exception as e:
    print("Enter valid input")
