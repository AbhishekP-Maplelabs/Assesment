"""
    Description: To sort the hyphen separated words alphabetically
"""
def sort_words(string):
    """
        This function sorts the hyphen separated words in alphabetical order
    """
    items=list(string.split('-'))
    flag=0
    for i in range(len(items)):
        for j in range(len(items)-i-1):
            if items[j]>items[j+1]:
                items[j], items[j+1] = items[j+1], items[j]
                flag=1
        if flag==0:
            break
    return '-'.join(items)
if __name__=="__main__":
    try:
        STRING=input("Enter a hyphen separated sequence of words: ")
        RESULT=sort_words(STRING)
        print(f"The words after sorting alphabeticallt are: {RESULT}")
    except Exception as e:
        print("Enter valid input")
