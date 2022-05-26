"""
description:To find the sum of the positive numbers skipping the negative numbers
"""
try:
    NUM=int(input("Enter the number of elements: "))
    LIST=[]
    SUM=0
    for i in range(0,NUM):
        element=int(input())
        LIST.append(element)
        if LIST[i]>0:
            SUM =SUM+LIST[i]
        else:
            i+=1
    print(f"The sum of positive numbers is: {SUM}")
except Exception as e:
    print("Run again and please enter the valid input")
