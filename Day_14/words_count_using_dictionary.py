"""
    Description: To count the words in string using dictionary
"""
def count_words_dictionary(string):
    """
        Function to count the words using dictionary.
    """
    words = []
    words = string.lower().split()
    frequency = [words.count(i) for i in words]
    my_dictionary = dict(zip(words, frequency))
    print("Dictionary Items :  ",  my_dictionary)
if __name__ == "__main__":
    try:
        STRING = input("Enter any String: ")
        count_words_dictionary(STRING)
    except ValueError as v:
        print("Enter valid input")
    except TypeError as t:
        print("Enter proper input")
