"""
    Description: To print the words which have the size as specified by user
"""
def word_length(number):
    """
        This function will print those words which has the length given by the user
    """
    LIST=[]
    LIST_1=[]
    for word in range(number):
        word=input()
        if word.isnumeric():
            print("Enter proper word")
            quit()
        else:
            LIST.append(word)
    print(f"Original list: {LIST}")
    LENGTH=int(input("Enter the length of string to extract"))
    for string in LIST:
        if len(string)==LENGTH:
            LIST_1.append(string)
    print(f"After extracting strings of specified length from the said list: {LIST_1}")
try:
    NUMBER=int(input("Enter the number of words in the list: "))
    word_length(NUMBER)
except Exception as e:
    print("Enter the valid input")
