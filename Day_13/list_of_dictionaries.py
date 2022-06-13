"""
    Description: to read the list
"""
def parse(dicct_list):
    """
        Function to read the list of dictionareis from the text file
    """
    my_dictionary = {}
    pairs = dicct_list.strip('{}').split(', ')
    for i in pairs:
        pair = i.split(': ')
        my_dictionary[pair[0].strip('\'\"\"')] = pair[1].strip('\'\"\"')
    return my_dictionary
if __name__ == "__main__":
    try:
        with open('D:/Work/dictionaries.txt','r',encoding="utf8") as TEXT_FILE:
            lines = TEXT_FILE.read().split('\n')
            for line in lines:
                if line != '':
                    dictionary = parse(line)
                    print(dictionary)
            TEXT_FILE.close()
    except ValueError as v:
        print("Something unexpected occurred!")
    except FileNotFoundError as t:
        print("Enter proper file name")
