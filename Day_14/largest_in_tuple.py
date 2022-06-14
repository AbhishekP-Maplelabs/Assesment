"""
    Description:To print the largest element in tuple.
"""
def largest_in_tuple(num_tuple):
    """
        Function to print the largest item in tuple.
    """
    largest=num_tuple[0]
    for element in range(1,len(num_tuple)):
        if num_tuple[element]>largest:
            largest=num_tuple[element]
    return largest
if __name__ == "__main__":
    try:
        NUMBER=int(input("Enter the length of tuple: "))
        TUPLE_LIST=[]
        for num in range(NUMBER):
            TUPLE_LIST.append(input())
        TUPLE=tuple(TUPLE_LIST)
        LARGEST=largest_in_tuple(TUPLE)
        print(f"The largest item in tuple is: {LARGEST}")
    except TypeError as t:
        print("Enter valid input")
    except ValueError as v:
        print("Enter proper values")
