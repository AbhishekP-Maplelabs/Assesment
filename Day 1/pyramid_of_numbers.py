"""
description: To print pyramid pattern using numbers based on numbsre of rows given
"""
try:
    num=int(input("Enter the numberof rows: "))
    for i in range(num):
        for j in range(num-i-1):
            print(" ",end="")
        for j in range(i,-1,-1):
            print(i+1,end=" ")
        print()
except Exception as e:
    print("Enter valid input")
        