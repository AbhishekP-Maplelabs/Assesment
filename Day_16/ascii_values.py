"""
    Description: Python program to print ASCII values of all characters in the string.
"""
def ascii_value(string):
    """
        Function to print the ASCII values of all the characters in the gtring.
    """
    for letter,i in enumerate (string):
        print(i)
        print(f"The ASCII value of letter {string[letter]} is: {ord(string[letter])}")
if __name__ == "__main__":
    STRING=input("Entwr the string: ")
    ascii_value(STRING)
