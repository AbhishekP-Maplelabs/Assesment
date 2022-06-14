"""
    Description: To count the number of words in the string
"""
def words_count(string):
    """
        Function to count the number of words in string entered.
    """
    count=1
    for word in string:
        if word  not in (' ','\n','\t'):
            count=count+1
    return count
if __name__ == "__main__":
    try:
        STRING=input("Enter the string: ").split()
        COUNT=words_count(STRING)
        print(f"The number of words in the given string are: {COUNT}")
    except TypeError as t:
        print("Enter valid input")
