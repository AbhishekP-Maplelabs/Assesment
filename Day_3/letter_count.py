"""
Description: To Read a Text File and Count the frequency of a Certain Letter Appears in the File.
"""
def letter_count(file_name):
    """
        This function counts the number of times a certain letter appers in the file.
    """
    key_letter=input("Enter letter to be searched:")
    k = 0
    with open(file_name, 'r',encoding="utf8") as file:
        for line in file:
            line = line.strip()
            line = line.lower().replace(".","")
            words = line.split()
            for i in words:
                for letter in i:
                    if letter==key_letter:
                        k=k+1
    return k
if __name__ == "__main__":
    try:
        FILE_NAME = input("Enter file name: ")
        RESULT=letter_count(FILE_NAME)
        print(f"Occurrences of the letter entered is: {RESULT}")
    except Exception as e:
        print("Enter proper input")
