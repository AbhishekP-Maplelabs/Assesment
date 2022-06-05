"""
description:To find the sum of the positive numbers skipping the negative numbers
"""
def positive_sum(number):
    """
        Function to print the sum of positive numbers in the list
    """
    num_list=[]
    addition=0
    for i in range(0,number):
        element=int(input())
        num_list.append(element)
        if num_list[i]>0:
            addition =addition+num_list[i]
        else:
            i+=1
    print(f"The sum of positive numbers is: {addition}")
if __name__ == "__main__":
    try:
        NUMBER=int(input("Enter the length of list"))
    except Exception as e:
        print("Run again and please enter the valid input")
