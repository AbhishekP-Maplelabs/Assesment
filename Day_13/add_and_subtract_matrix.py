"""
    Description: Addition and subtraction of two matrices
"""
def add_and_subtract_matrix(rows,columns):
    """
        Function to add and subtract two matrices
    """
    print("Enter the elements of First Matrix:")
    matrix_a= [[int(input()) for i in range(columns)] for i in range(rows)]
    print("First Matrix is: ")
    for num in matrix_a:
        print(num)
    print("Enter the elements of Second Matrix:")
    matrix_b= [[int(input()) for i in range(columns)] for i in range(rows)]
    for number in matrix_b:
        print(number)
    addition=[[0 for i in range(columns)] for i in range(rows)]
    subtraction=[[0 for i in range(columns)] for i in range(rows)]
    for i in range(rows):
        for j in range(columns):
            addition[i][j] = matrix_a[i][j]+matrix_b[i][j]
    print("The Sum of Above two Matrices is : ")
    for summation in addition:
        print(summation)
    for i in range(rows):
        for j in range(columns):
            subtraction[i][j] = matrix_a[i][j]-matrix_b[i][j]
    print("The difference of Above two Matrices is : ")
    for difference in subtraction:
        print(difference)
if __name__ == "__main__":
    try:
        ROWS = int(input("Enter the Number of rows : " ))
        COLUMNS = int(input("Enter the Number of Columns: "))
        add_and_subtract_matrix(ROWS,COLUMNS)
    except ValueError as v:
        print("Enter valid input")
    except TypeError as t:
        print("enter proper values")
        