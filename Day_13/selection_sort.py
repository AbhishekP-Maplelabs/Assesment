"""
    Description: Implementation of selection sort
"""
def selection_sort(num_list,list_length):
    """
        Sort the list of numbers using selection sort algorithm
    """
    for i in range(list_length):
        min_value_index=i
        for j in range(i+1,list_length):
            if num_list[j]<num_list[min_value_index]:
                min_value_index=j
        (num_list[i],num_list[min_value_index])=(num_list[min_value_index],num_list[i])

if __name__=="__main__":
    try:
        NUMBER=int(input("Enter the length of list: "))
        TEST_LIST=[]
        print("Enter the numbers: ")
        for num in range(NUMBER):
            TEST_LIST.append(int(input()))
        LENGTH=len(TEST_LIST)
        selection_sort(TEST_LIST,LENGTH)
        print(f"list after sorting is: {TEST_LIST}")
    except TypeError  as e:
        print("Enter valid input")
    except ValueError as v:
        print("Enter proper list")
