"""
    Description: To remove multiple elements from list
"""
def remove_from_list(num_list):
    """
        Function to remove numbers which are didvisible by 2.
    """
    for num,i in enumerate(num_list):
        if num_list[num] % 2 ==0:
            num_list.remove(num_list[num])
        i+=1
    print(F"list after removing the elements is: {num_list}")
if __name__ == "__main__":
    try:
        NUMBER=int(input("Enter the length of list: "))
        LIST=[]
        for number in range(NUMBER):
            LIST.append(int(input()))
        remove_from_list(LIST)
    except ValueError as v:
        print("Enter valid input")
    except TypeError as t:
        print("Enter proper values")
