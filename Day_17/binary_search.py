"""
module:3
description:To find the element using binary search algorithm
"""
def binary_search(num_list, low, high, value):
    """
        Function for binary search
    """
    if high >= low:
        mid = (high + low) // 2
        if num_list[mid] == value:
            return mid
        if num_list[mid] > value:
            return binary_search(num_list, low, mid - 1, value)
        return binary_search(num_list, mid + 1, high, value)
    return -1
LIST = []
NUMBER = int(input("Enter the list size: "))
for i in range (NUMBER):
    numbers=int(input())
    LIST.append(numbers)
key=int(input("Enter the key number to search: "))
result = binary_search(LIST, 0, len(LIST)-1, key)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")
