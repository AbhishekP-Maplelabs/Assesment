"""
    Python program to print Floyd's triangle.
"""
def floyds_triangle(rows):
    """
        Function to print floyd's triangle from given number of rows.
    """
    number = 1
    for i in range(rows):
        for j in range(i+1):
            print(number, end=" ")
            number = number+1
            j+=1
        print()
if __name__ == "__main__":
    try:
        ROWS=int(input("Enter the number of rows: "))
        floyds_triangle(ROWS)
    except ValueError as v:
        print("Enter valid input")
        