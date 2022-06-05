"""
    Description: To find the largest and smallest number in the tuple
"""
def largest_smallest(number_1):
    """
        This function will print the largesr and smallest number in the tuple
    """
    num_list=[]
    for i in range(number_1):
        num_list.append(input())
    num_tuple=tuple(num_list)
    print(f"The entered tuple is: {num_tuple}")
    largest=num_tuple[0]
    smallest=num_tuple[0]
    for i in range(1,len(num_tuple)):
        if largest<num_tuple[i]:
            largest=num_tuple[i]
        if smallest>num_tuple[i]:
            smallest=num_tuple[i]
    print(f"The largest item in the tuple is: {largest}")
    print(f"The smallet item in the tuple is: {smallest}")
if __name__ == "__main":
    try:
        NUMBER=int(input("ENter the number of elements: "))
        print("Enter the elements:")
        largest_smallest(NUMBER)
    except Exception as e:
        print("Enter valid input")
