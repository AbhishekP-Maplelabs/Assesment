"""
    Description: plus pattern.
"""
def plus_pattern(number):
    """
        Function to print plus pattern from given number if lines.
    """
    for i in range (1,2*number):
        for j in range (1,2*number):
            if number in (i,j):
                print(" * ",end='')
            else:
                print("   ",end='')
        print()
if __name__ == "__main__":
    NUMBER=int(input("Enter the number of lines: "))
    plus_pattern(NUMBER)
