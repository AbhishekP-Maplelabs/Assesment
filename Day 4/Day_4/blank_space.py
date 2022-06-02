"""
    Descriptin: To count the number of blank spaces in a text file
"""
def counter(file_name):
    """
        This function will count the number of blank spaces in a text file
    """
    blank_space=0
    with open(file_name, 'r',encoding="utf8") as file:
        for line in file:
            for letter in line:
                if letter == ' ':
                    blank_space+=1
        print('Number of spaces in text file: ', blank_space)
if __name__ == '__main__':
    try:
        FileName = input("Enter the file name: ")
        counter(FileName)
    except FileNotFoundError as e :
        print('File not found')
