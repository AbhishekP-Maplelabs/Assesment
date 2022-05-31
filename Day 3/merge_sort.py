"""
    description: To implement merge sort algorithm to sort the elements in the list
"""
def merge_sort(my_list):
    """
        This function demonstrates sorting using merge sort algorithm.
    """
    if len(my_list) > 1:
        mid = len(my_list) // 2
        left = my_list[:mid]
        right = my_list[mid:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                my_list[k] = left[i]
                i += 1
            else:
                my_list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            my_list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            my_list[k]=right[j]
            j += 1
            k += 1
try:
    NUMBER=int(input("Enter the number of elements: "))
    LIST = []
    for l in range(NUMBER):
        LIST.append(int(input()))
    print(f"The entered list is :{LIST}")
    merge_sort(LIST)
    print(f"The sorted list is : {LIST}")
except Exception as e:
    print("Enter the valid input")
