"""
    Description: To convert decimlal value to binary
    and check wheather the binary value is palindrome or not
"""
def decimal_to_binary(number):
    """
        This function returns true if the binary value of corresponding decimal
        is palindrome else it returns false.
    """
    num_list=[]
    while number>0:
        dig=number%2
        num_list.append(dig)
        number=number//2
    num_list.reverse()
    print("Binary Equivalent is: ")
    for num in num_list:
        print(num,end=" ")
    for i in range(0, int(len(num_list)/2)):
        if num_list[i] != num_list[len(num_list)-i-1]:
            return False
    return True


NUMBER=int(input("Enter a number: "))
RESULT=decimal_to_binary(NUMBER)
if RESULT:
    print("Binary value is palindrome")
else:
    print("Binary value is not palindrome")
