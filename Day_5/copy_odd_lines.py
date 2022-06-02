"""
    Description: To read contents of a file and copy only the content of odd lines into new file.
"""
def copy_odd_lines(file_name):
    """
        Function to copy odd lines from one file to another
    """
    with open(file_name, 'r',encoding="utf8") as file:
        with open('file_1.txt', 'w',encoding="utf8") as new_file:
            count = file.readlines()
            for i in enumerate(len(count)):
                if i % 2 == 0:
                    new_file.write(count[i])
                else:
                    pass
    new_file.close()
    with open('file_1.txt', 'r',encoding="utf8") as new_file:
        count1 = new_file.read()
    print(count1)
    file.close()
    new_file.close()
if __name__=="__main__":
    try:
        FILE="file.txt"
        copy_odd_lines(FILE)
    except Exception as e:
        print("provide valid input")
