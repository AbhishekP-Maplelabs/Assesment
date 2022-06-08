"""
    Description: To print the frequency of characters if the string.
"""
def frequency(string):
    """
        Function to count characters frequency in a string.
    """
    char_freq={}
    for letter in string:
        if letter in char_freq:
            char_freq[letter]+=1
        else:
            char_freq[letter]=1
    print(char_freq)
if __name__ == "__main__":
    STRING=input("Enter the string: ")
    frequency(STRING)
