"""
    Description: To print the count of positive and negative integers.
"""
def positive_and_negative_numbers(num_tuple):
    """
        Function to find the count of positive and negative numbers in tuple
    """
    positive_count=0
    negative_count=0
    for num,i in enumerate(num_tuple):
        if num_tuple[num]>=0:
            positive_count+=1
            i+=1
        else:
            negative_count+=1
    print(f"Count of positive numbers is: {positive_count}")
    print(f"Count of negative numbers is: {negative_count}")
if __name__ == "__main__":
    try:
        NUMBER=int(input("Enter the length of list: "))
        LIST=[]
        print("Enter the numbers:")
        for number in range(NUMBER):
            LIST.append(int(input()))
        TUPLE=tuple(LIST)
        positive_and_negative_numbers(TUPLE)
    except ValueError as v:
        print("Enter valid input")
    except IndexError as I:
        print("run again and give proper values")
