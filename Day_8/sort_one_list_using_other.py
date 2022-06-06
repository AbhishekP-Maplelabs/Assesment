"""
    Description : To sort one list using other list of same length
"""
def sort(list_2,list_1):
    """
        Function to sort the frist list using second list.
    """
    zipped_pairs = zip(list_1, list_2)
    sorted_list = [x for _, x in sorted(zipped_pairs)]
    return sorted_list
if __name__ == "__main__":
    try:
        NUMBER=int(input("ENter the length of list: "))
        LIST_1=[]
        LIST_2=[]
        print("Enter the elements in first list ")
        for i in range(NUMBER):
            LIST_1.append(int(input()))
        print("Enter the elements in second list ")
        for i in range(NUMBER):
            LIST_2.append(input())
        print(LIST_1)
        print(LIST_2)
        RESULT=sort(LIST_1,LIST_2)
        print(f"the sorted list is: {RESULT}")
    except Exception as e:
        print("Enter valid input")
