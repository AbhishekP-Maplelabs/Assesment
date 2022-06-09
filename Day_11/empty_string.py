"""
    Description: To check if the string will be empty after recurive deletion.
"""
def check_string(string, sub_str):
    """
        Funcion to delete the sub string from main string
        to check if the string will be empty after recursive deletion
    """
    while len(string) > 0:
        idx = string.find(sub_str)
        if idx == -1:
            break
        string = string.replace(sub_str, "", 1)
    return len(string) == 0
if __name__ == "__main__":
    STRING = input("Enter the string: ")
    SUB_STRING = input("Enter the string to be sliced: ")
    if check_string(STRING,SUB_STRING):
        print("The string can become empty ")
    else:
        print("The string cannot become empty ")
