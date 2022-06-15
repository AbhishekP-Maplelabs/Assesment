"""
    Description: Python program to Print anagrams together
"""
def anagram_words(num_list):
    """
        Function to print the anagrams together.
    """
    my_dictionary = {}
    for val in num_list:
        key = ''.join(sorted(val))
        if key in my_dictionary:
            my_dictionary[key].append(val)
        else:
            my_dictionary[key] = []
            my_dictionary[key].append(val)
    result = ""
    for key,value in my_dictionary.items():
        result = result + ' '.join(value) + ' '
    return result
if __name__ == "__main__":
    try:
        NUMBER=int(input("Enter the length of list: "))
        LIST=[]
        for num in range(NUMBER):
            LIST.append(input())
        print("Words: ",LIST)
        print("Anagram: ",anagram_words(LIST))
    except ValueError as v:
        print("Enter valid input")
