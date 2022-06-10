"""
    Description: To separate the positive and negative numbers from list.
"""
def positive_negative_numbers(num_list):
    """
        Function to separate the positive and negative numbers from list.
    """
    positive_list=[]
    negative_list=[]
    for number,j in enumerate(num_list):
        if num_list[number]>=0:
            positive_list.append(num_list[number])
            j+=1
        else:
            negative_list.append(num_list[number])
            j+=1
    print(f"the list of positive numbers is{positive_list}")
    print(f"the list of negative numbers is{negative_list}")
if __name__ == "__main__":
    try:
        NUMBER=int(input("Enter the length of list: "))
        LIST=[]
        print("Enter the numbers: ")
        for num in range(NUMBER):
            LIST.append(int(input()))
        positive_negative_numbers(LIST)
    except ValueError as v:
        print("Enter valid input")
    except TypeError as t:
        print("Enter proper list")
    except IndexError as i:
        print("Enter numbers within index range")
