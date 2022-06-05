"""
description: To print pyramid pattern using numbers based on numbsre of rows given
"""
def pyramid_of_numbers(number):
    """
        function to print the pyramid using the numbers given up to 9
    """
    for i in range(number):
        for j in range(number-i-1):
            print(" ",end="")
        for j in range(i,-1,-1):
            print(i+1,end=" ")
        print()
if __name__ == "__main__":
    NUMBER=int(input("Enter the number of rows: "))
    if 1<NUMBER<10:
        pyramid_of_numbers(NUMBER)
    else:
        print("Enter numbers between 1 and 10")
