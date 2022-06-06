"""
    Description : Transpose of matrix
"""
def transpose_matrix(row,column):
    """
        Function to transpose the matrix.
    """
    print("Enter the elements of Matrix:")
    matrix= [[int(input()) for i in range(column)] for i in range(row)]
    print("Entered Matrix is:   ")
    for num in matrix:
        print(num)
    result =[[0 for i in range(row)] for j in range(column)]
    for rows in range(row):
        for columns in range(column):
            result[columns][rows] = matrix[rows][columns]
    print("Transpose matrix is: ")
    for r in result:
        print(r)
if __name__ == "__main__":
    ROWS = int(input("Enter the Number of rows : " ))
    COLUMNS=int(input("Enter the number of columns: "))
    transpose_matrix(ROWS,COLUMNS)
