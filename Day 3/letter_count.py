"""
Description: To Read a Text File and Count the frequency of a Certain Letter Appears in the File.
"""
def letter_count():
    """
        This function counts the number of times a certain letter appers in the file. 
    """
    fname = input("Enter file name: ")
    l=input("Enter letter to be searched:")
    k = 0
    with open(fname, 'r') as f:
        for line in f:
            line = line.strip()
            line = line.lower().replace(".","")
            words = line.split()
            for i in words:
                for letter in i:
                    if letter==l:
                        k=k+1
    return k
try:
    RESULT=letter_count()
    print(f"Occurrences of the letter entered is: {RESULT}")
except Exception as e:
    print("Enter proper input")
