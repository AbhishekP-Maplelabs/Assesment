"""
    description: Python program to remove even numbers from list.
"""
def remove_even_number(num_list):
    """
        Function to remove even numbers from list.
    """
    for number in num_list.copy():
        if number % 2 == 0:
            num_list.remove(number)
    print(f"The list after removing even numbers is: {num_list}")
if __name__ == "__main__":
    try:
        NUMBER=int(input("Enter the length of list: "))
        LIST=[]
        for num in range(NUMBER):
            LIST.append(int(input()))
        remove_even_number(LIST)
    except ValueError as v:
        print("Enter valid input")
    except TypeError as t:
        print("provide proper values as input")
