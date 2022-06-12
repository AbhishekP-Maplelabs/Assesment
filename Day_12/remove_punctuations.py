"""
    Description: To remove punctuation from a given string
"""
def remove_panctuation_marks(string):
    """
        Function to remove punctuation
    """
    punctuations = '''!()-[]{};:'"\r<>,./?@#$%^&*_~'''
    for char in string.lower():
        if char in punctuations:
            string = string.replace(char, "")
    print(f"The string after removing the punctuations is: {string}")
if __name__ == "__main__":
    try:
        STRING = input("Enter the string")
        remove_panctuation_marks(STRING)
    except ValueError as v:
        print("Enter valid input")
        