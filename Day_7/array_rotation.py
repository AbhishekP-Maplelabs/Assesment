"""
    Decsription: To ratate the numbers in array from given position
"""
def array_rotation(arr,pos):
    """
        This function rotates the numbers in array from entered position
    """
    for first in range(0, pos):
        first = arr[0]
        for j in range(0, len(arr)-1):
            arr[j] = arr[j+1]
        arr[len(arr)-1] = first
    print()
    print("Array after left rotation: ")
    for num in range (0,len(arr)):
        print(arr[num],end=' ')
NUMBER=int(input("Enter the length of array: "))
ARRAY=[]
print("Enter numbers")
for i in range(NUMBER):
    ARRAY.append(int(input()))
print(f"Entered array is: {ARRAY}")
POSITION=int(input("ENter the position from which tha array to be rotated: "))
array_rotation(ARRAY,POSITION)
