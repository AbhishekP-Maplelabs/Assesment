"""
    Description: To find the largest and smallest number in the tuple
"""
def largest_smallest(number_1):
    """
        This function will print the largesr and smallest number in the tuple
    """
    LIST=[]
    for i in range(number_1):
        LIST.append(input())
    TUPLE=tuple(LIST)
    print(f"The entered tuple is: {TUPLE}")
    LARGEST=TUPLE[0]
    SMALLEST=TUPLE[0]
    for i in range(1,len(TUPLE)):
        if LARGEST<TUPLE[i]:
            LARGEST=TUPLE[i]
        if SMALLEST>TUPLE[i]:
            SMALLEST=TUPLE[i]
    print(f"The largest item in the tuple is: {LARGEST}")
    print(f"The smallet item in the tuple is: {SMALLEST}")
try:
    NUMBER=int(input("ENter the number of elements: "))
    print("Enter the elements:")
    largest_smallest(NUMBER)
except Exception as e:
    print("Enter valid input")
