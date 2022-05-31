"""
    To iterate over the range of numbers and printing for multiples of three , print "Maple" instead of the number
     and for the multiples of five, print "Labs".
     For numbers which are multiples of both three and five print "MapleLabs".
"""
def print_words(number_range):
    """
    This function iterates over the given range of numbers and For multiples of three , print "Maple" instead of the number
     and for the multiples of five, print "Labs".
     For numbers which are multiples of both three and five print "MapleLabs".
    """
    for i in range(1,number_range+1):
        if ((i % 3==0)and (i % 5==0)):
            print("Maple Labs")
        elif i % 5==0:
            print("Labs")
        elif i % 3==0:
            print("Maple")
        else:
            print(i)
try:
    number=int(input("Enter the range of the number to be iterated: "))
    print_words(number)
except Exception as e:
    print("Enter valid input")
