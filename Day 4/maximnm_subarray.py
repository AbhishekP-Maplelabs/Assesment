"""
    Description: To find the sum of the elements in subarray which has maximum values
"""
def max_crossing_sum(my_array, low, mid, high):
    """
        This function computes the sum of elements on the left part of the list
    """
    sum_elements = 0
    sum_left_elements = -10000
    for i in range(mid, low-1, -1):
        sum_elements = sum_elements + my_array[i]
    if sum_elements > sum_left_elements:
        sum_left_elements = sum_elements
    sum_elements = 0
    sum_right_elements = -1000
    for i in range(mid + 1, high + 1):
        sum_elements = sum_elements + my_array[i]
        if sum_elements > sum_right_elements:
            sum_right_elements = sum_elements
    return max(sum_left_elements + sum_right_elements, sum_left_elements, sum_right_elements)
def max_sub_array_sum(my_array, low, high):
    """
        This function computes sum of every sub array
    """
    if low == high:
        return my_array[low]
    mid = (low + high) // 2
    return max(max_sub_array_sum(my_array, low, mid), max_sub_array_sum(my_array, mid+1, high), max_crossing_sum(my_array, low, mid, high))
try:
    NUMBER=int(input("Enter the length of list: "))
    my_list = []
    for i in range(NUMBER):
        my_list.append(int(input()))
    list_length = len(my_list)
    print("The list is :")
    print(my_list)
    max_sum = max_sub_array_sum(my_list, 0, list_length-1)
    print("The maximum contiguous sum is ")
    print(max_sum)
except Exception as e:
    print("Enter valid input")
    