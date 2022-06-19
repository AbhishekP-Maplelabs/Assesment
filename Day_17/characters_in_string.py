"""
    Description: Python program to count the characters in the string
"""
def count_character(string):
    """
        Function to count the characters in the string
    """
    count=0
    for character,i in enumerate(string):
        print(i,end=',')
        if string[character] != " ":
            count+=1
    return count
if __name__ == "__main__":
    try:
        STRING=input("Enter the string: ")
        COUNT=count_character(STRING)
        print(f"The total number of characters in the string are: {COUNT}")
    except ValueError as v:
        print("Enter the valid iinput")
