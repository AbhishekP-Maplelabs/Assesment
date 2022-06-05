"""
    description: To print the words which has the first characters as given by the user
"""
import sys
def first_char(number):
    """
        This function will print the words which starts with first character as given by user
    """
    string_list=[]
    string_list_1=[]
    for word in range(number):
        word=input()
        if word.isnumeric():
            print("Enter the proper word")
            sys.exit()
        else:
            string_list.append(word)
    print(f"Original list: {string_list}")
    char=str(input("Enter the first character of words to be printed: "))
    for string in string_list:
        if string[0]==char:
            string_list_1.append(string)
    print(f"Items start with {char} from the said list: {string_list_1}")
if __name__ == "__main__":
    try:
        NUMBER=int(input("Enter the number of words in list: "))
        first_char(NUMBER)
    except Exception as e:
        print("Enter the valid input")
