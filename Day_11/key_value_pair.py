"""
    Description: To count the occurence of key value pair in the file
"""
def key_value_pair(file_name):
    """
        Function to count the key value pairs in the text file.
    """
    with open(file_name,"r",encoding="utf8")as file:
        dictionary ={}
        for res in file:
            res = res.strip()
            lines = res.split()
            for line in lines:
                if line in dictionary:
                    dictionary[line] = dictionary[line]+1
                else:
                    dictionary[line] = 1
        file.close()
    for key in list(dictionary.keys()):
        print(f"The count of {key} is {dictionary[key]}")
if __name__ == "__main__":
    try:
        FILE_NAME="D:/Work/Practice/module_1/Module_2/assesment/Day_11/key.txt"
        key_value_pair(FILE_NAME)
    except FileNotFoundError as e:
        print("enter valid input")
