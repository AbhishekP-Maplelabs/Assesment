"""
    Python program to sort 0s, 1s and 2s in ascending order in single pass.
"""
def sort012( num_list, length):
    """
        Function to sort the list
    """
    low = 0
    high = length - 1
    mid = 0
    while mid <= high:
        if num_list[mid] == 0:
            num_list[low], num_list[mid] = num_list[mid], num_list[low]
            low = low + 1
            mid = mid + 1
        elif num_list[mid] == 1:
            mid = mid + 1
        else:
            num_list[mid], num_list[high] = num_list[high], num_list[mid]
            high = high - 1
    return num_list
if __name__ == "__main__":
    try:
        NUMBER=int(input("Enter the length of list: "))
        LIST=[]
        for num in range(NUMBER):
            LIST.append(int(input()))
        RESULT = sort012( LIST, len(LIST))
        print ("List after sorting :",)
        for number in RESULT:
            print(number,end=' ')
    except ValueError as v:
        print("Enter valid input")
    except TypeError as t:
        print("Enter correct values")
