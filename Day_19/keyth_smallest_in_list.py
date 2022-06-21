"""
    Description: Python program to find the (KEY)th smallest number in the list.
"""
import sys
def smallest_in_list(num_list,key):
    """
        Function to find the (kry)th smallest number in the list.
    """
    num_list.sort()
    return num_list[key-1]
if __name__ == "__main__":
    try:
        NUMBER=int(input("Enter the length of list: "))
        LIST=[]
        for num in range(NUMBER):
            LIST.append(int(input()))
        KEY=int(input("Enter the key: "))
        if KEY>NUMBER:
            print("Enter valid key")
            sys.exit()
        RESULT=smallest_in_list(LIST,KEY)
        print(f"The {KEY} smallest number is: {RESULT}")
    except ValueError as v:
        print("Enter valid input")
