"""
    Description: python program to print N largest elements from list.
"""
def largest_elements(num_list,number):
    """
        Function to print N largest elements.
    """
    final_list=[]
    for i in range(0, number):
        max1 = 0
        for num ,k in enumerate(num_list):
            if num_list[num] > max1:
                max1 = num_list[num]
            k+=1
        num_list.remove(max1)
        final_list.append(max1)
        i+=1
    print(f"The  {number} largest elements are: {final_list}")
if __name__ == "__main__":
    try:
        LENGTH=int(input("Enter the length of list: "))
        LIST=[]
        for element in range(LENGTH):
            LIST.append(input())
        NUMBER=int(input("Enter number of elements: "))
        largest_elements(LIST,NUMBER)
    except ValueError as v:
        print("Enter valid input")
    except TypeError as t:
        print("Provide proper values")
        