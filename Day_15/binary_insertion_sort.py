"""
    Description: Python program to implement binary insertion sort.
"""
def insertion_sort(num_list):
    """
        Function for insertion sort.
    """
    for i in range(1, len(num_list)):
        temp = num_list[i]
        pos = binary_search(num_list, temp, 0, i) + 1
        for k in range(i, pos, -1):
            num_list[k] = num_list[k - 1]
        num_list[pos] = temp
def binary_search(num_list, key, start, end):
    """
        Function for binary search.
    """
    if end - start <= 1:
        if key < num_list[start]:
            return start - 1
        return start
    mid = (start + end)//2
    if num_list[mid] < key:
        return binary_search(num_list, key, mid, end)
    if num_list[mid] > key:
        return binary_search(num_list, key, start, mid)
    return mid

NUMBER=int(input("Enter the length of list: "))
LIST = []
for num in range(NUMBER):
    LIST.append(int(input()))
LENGTH = len(LIST)
insertion_sort(LIST)
print("Sorted array is:")
for number in range(LENGTH):
    print(LIST[number],end=" ")
