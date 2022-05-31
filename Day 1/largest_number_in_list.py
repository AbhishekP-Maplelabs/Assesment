"""
description: To find the largest number in the list without using built in libraries
"""
try:
    num=int(input("Enter the number of elements in the list: "))
    LIST=[]
    for i in range(num):
        elem=input()
        LIST.append(elem)
    max_value=LIST[0]
    INDEX=0
    for j in range(len(LIST)):
        if LIST[i]>max_value:
            max_value=LIST[i]
            INDEX=i
    print(f"The Largest Element in this List is: {max_value} ")
    print(f"The Index position of the Largest Element is: {INDEX}")
except Exception as e:
    print("Enter the valid input")
