"""
    Description: to create the dictionary to print in (x x*x) form.
"""
def create_dictionary(num_range):
    """
        Function to Create Dictionary of Numbers 1 to n in (x, x*x) form.
    """
    my_dictionary={}
    for num in range(1,num_range+1):
        my_dictionary[num]=num*num
        num+=1
    print(f"Created dictionary is: {my_dictionary}")
if __name__ == "__main__":
    try:
        NUM_RANGE=int(input("Enter the number range"))
        create_dictionary(NUM_RANGE)
    except ValueError as v:
        print("Enter valid input")
    except TypeError as t:
        print("Enter proper input ")
