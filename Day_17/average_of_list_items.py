"""
    Description: Python program to print the average of list items.
"""
def item_average(num_list):
    """
        Function to find the average of list items
    """
    total=0
    for number,i in enumerate(num_list):
        total=total+num_list[number]
        i+=1
    average=total//len(num_list)
    return average
if __name__ == "__main__":
    try:
        NUMBER=int(input("Enter the length of list: "))
        LIST=[]
        for num in range(NUMBER):
            LIST.append(int(input()))
        AVERAGE=item_average(LIST)
        print(f"The average of the items in the list is: {AVERAGE}")
    except ValueError as v:
        print("Enter valid input")
    except TypeError as t:
        print("provide proper inputs")
        