"""
description: To find the largest number in the list without using built in libraries
"""
def largest_in_list(num_list):
    """
        function to find largest number in list without using built in libraries
    """
    max_value=num_list[0]
    index=0
    for j,number in enumerate (num_list):
        if number>max_value:
            max_value=number
            index=j
    print(f"The Largest Element in this List is: {max_value} ")
    print(f"The Index position of the Largest Element is: {index}")
if __name__ == "__main__":
    try:
        num=int(input("Enter the number of elements in the list: "))
        LIST=[]
        for i in range(num):
            elem=input()
            LIST.append(elem)
        largest_in_list(LIST)
    except Exception as e:
        print("Enter valid input")
