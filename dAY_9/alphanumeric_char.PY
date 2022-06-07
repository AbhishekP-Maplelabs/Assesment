"""
    Description: To check the string for if the last character is alphanumeric or not
"""
def check_string(string):
    """
        Function to check the entered string for alphanumeric as its last character.
    """
    if string[-1].isnumeric():
        print("accepted")
    else:
        print("rejected")
if __name__ == "__main__":
    STRING=input("Enter the string: ")
    check_string(STRING)
