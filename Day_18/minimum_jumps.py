"""
    Description: Python program to find the minimum number of jumps to reach the end of the list.
"""
def min_jumps(arr, start, end):
    """
        Function to find the number of jumps.
    """
    if end == start:
        return 0
    if arr[start] == 0:
        return float('inf')
    minimum = float('inf')
    for i in range(start + 1, end + 1):
        if i < start + arr[start] + 1:
            jumps = min_jumps(arr, i, end)
            if (jumps != float('inf') and jumps + 1 < minimum):
                minimum = jumps + 1
    return minimum
NUMBER=int(input("Enter the length of list: "))
LIST=[]
print("Enter the numbers")
for num in range(NUMBER):
    LIST.append(int(input()))
RESULT=min_jumps(LIST, 0, len(LIST)-1)
print(f"The minimum jumps to reach the end :{RESULT}")
