"""
    Description: Python program to print even length words from the string.
"""
def even_length_words(string):
    """
        Function to print even length words from string.
    """
    even_word_list=[]
    for word in string:
        if len(word) % 2 == 0:
            even_word_list.append(word)
    print(f"The even length words from the string are: {even_word_list}")
if __name__ == "__main__":
    try:
        STRING=input("Enter the string: ").split()
        even_length_words(STRING)
    except ValueError as v:
        print("Enter valid input")
