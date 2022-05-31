"""
    description: To print the words which has the first characters as given by the user
"""
def first_char(number):
    """
        This function will print the words which starts with first character as given by user
    """
    LIST=[]
    LIST_1=[]
    for word in range(number):
        word=input()
        if word.isnumeric():
            print("Enter the proper word")
            quit()
        else:
            LIST.append(word)
    print(f"Original list: {LIST}")
    CHAR=str(input("Enter the first character of words to be printed: "))
    for string in LIST:
        if string[0]==CHAR:
            LIST_1.append(string)
    print(f"Items start with {CHAR} from the said list: {LIST_1}")
try:
    NUMBER=int(input("Enter the number of words in list: "))
    first_char(NUMBER)
except Exception as e:
    print("Enter the valid input")
