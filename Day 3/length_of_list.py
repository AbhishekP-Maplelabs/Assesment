"""
    description: To find the length of list using recurrsion
"""
def list_length(my_list_1):
    """
        This function demonstrates to find the length of list by recurrsion
    """
    if not my_list_1:
        return 0
    return 1 + list_length(my_list_1[1::2]) + list_length(my_list_1[2::2])
try:
    NUMBER=int(input("Enter the number of elements: "))
    my_list = []
    for i in range(NUMBER):
        my_list.append(input())
    print("The list is :")
    print(my_list)
    print(f"The length of the string is : {list_length(my_list)}")
except Exception as e:
    print("Please enter the valid input")
