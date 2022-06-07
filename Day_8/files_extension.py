"""
    Description:To find the files of the given extension in the directory
"""
import os
def file_name(directory):
    """
        Function to find the files with given extension.
    """
    files_available=[]
    for files_name in os.listdir(directory):
        if not files_name.endswith('.txt'):
            continue
        files_available.append(files_name)
    return files_available
if __name__=='__main__':
    try:
        PATH=input("Enter the path of the destination of files")
        result=file_name(PATH)
        print(f" The file is : \n{result}")
    except Exception as e:
        print("Enter valid input")
