"""
    Description: To print dimond pattern using given number of rows.
"""
def dimond_pattern(rows):
    """
        Function to print diamond number pattern using for loop.
    """
    upper = 2 * rows - 2
    for row in range(rows):
        for j in range(upper):
            print(end=" ")
            j+=1
        upper = upper - 1
        for j in range(0, row + 1):
            print(row+1, end=" ")
        print("")
    lower = rows - 2
    for i in range(rows, -1, -1):
        for row in range(lower, 0, -1):
            print(end=" ")
        lower = lower + 1
        for j in range(0, i + 1):
            print(i+1, end=" ")
        print("")
if __name__ == "__main__":
    try:
        ROWS=int(input("Enter number of rows between 2 and 9 : "))
        dimond_pattern(ROWS)
    except ValueError as v:
        print("Enter valid input")
