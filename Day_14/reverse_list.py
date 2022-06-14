"""
    Description: To print the list in reverse order
"""
def reverse_the_list(number):
    """
        Function to print the list in reverse order
    """
    num_list=[]
    for num in range(number):
        num_list.append(int(input()))
    reverse_list=[]
    for num in range(len(num_list),0,-1):
        reverse_list.append(num)
    print(reverse_list)
if __name__ == "__main__":
    try:
        NUMBER=int(input("Enter the length of list: "))
        reverse_the_list(NUMBER)
    except ValueError as v:
        print("Enter valid input")
