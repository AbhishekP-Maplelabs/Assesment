"""
    Description: To print the distinct words from the list given by the user
"""
def unique(list1):
    """
        This function will prints the unique words out of the list given by the user
    """
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    print(len(unique_list))
    for i in range(len(unique_list)):
        print(f"{unique_list[i]} :1")
try:
    NUMBER=int(input("Input number of words: "))
    LIST=[]
    for word in range(NUMBER):
        word=input()
        if word.isnumeric():
            print("Input the words: ")
            quit()
        else:
            LIST.append(word)
    unique(LIST)
except Exception as e:
    print("Enter valid input")
