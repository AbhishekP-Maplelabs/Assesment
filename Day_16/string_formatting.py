"""
    Python program to print the tuple using string formatting.
"""
NUMBER=int(input("Enter the length of tuple: "))
LIST=[]
for num in range(NUMBER):
    LIST.append(int(input()))
TUPLE=tuple(LIST)
print(f"Tuple Items are: {format(TUPLE)}")
