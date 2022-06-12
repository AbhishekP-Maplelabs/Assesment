"""
    Description: To print the odd numbers in the tuple.
"""
def odd_number(num_tuple):
    """
        Function to print the odd numbers in the tuple.
    """
    odd_list=[]
    for num,i in enumerate(num_tuple):
        if num_tuple[num]%2 != 0:
            odd_list.append(num_tuple[num])
        else:
            i+=1
    odd_num_tuple=tuple(odd_list)
    print("odd numbers in the tuple are:")
    print(odd_num_tuple)
if __name__ == "__main__":
    try:
        NUMBER=int(input("Enter the length of list: "))
        NUM_LIST=[]
        print("Enter the numbers: ")
        for element in range(NUMBER):
            NUM_LIST.append(int(input()))
        INPUT_TUPLE=tuple(NUM_LIST)
        odd_number(INPUT_TUPLE)
    except ValueError as e:
        print("Enter valid input")
