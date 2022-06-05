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
        iterator_1 = 0
        iterator_2 = 0
        iterator = 0
        while iterator_1 < len(left) and iterator_2 < len(right):
            if left[iterator_1] <= right[iterator_2]:
                my_list[iterator] = left[iterator_1]
                iterator_1 += 1
            else:
                my_list[iterator] = right[iterator_2]
                iterator_2 += 1
            iterator += 1
        while iterator_1 < len(left):
            my_list[iterator] = left[iterator_1]
            iterator_1 += 1
            iterator += 1
        while iterator_2 < len(right):
            my_list[iterator]=right[iterator_2]
            iterator_2 += 1
            iterator += 1
if __name__ == "__main__":
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
