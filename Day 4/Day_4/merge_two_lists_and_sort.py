"""
    Description: To merge two lists and sort the final list
"""
def merge_list_and_sort(list_1, list_2):
    """
        This function will take two lists as input and merges them and sort the resultant list
    """
    merge_list = list_1 + list_2
    print("merged list is: ", merge_list)
    flag = 0
    for num in range(len(merge_list)):
        for number in range(len(merge_list)-num-1):
            if merge_list[number] > merge_list[number+1]:
# swap the numbers
                merge_list[number], merge_list[number+1] = merge_list[number+1], merge_list[number]
                flag = 1
        if flag==0:
# means nothing was swapped
            break
    print(f"Merged and sorted list is : {merge_list}")
if __name__=="__main__":
    try:
        NUMBER_1=int(input("Enter the number of elements in first list: "))
        LIST_1=[]
        for i in range(NUMBER_1):
            LIST_1.append(int(input()))
        print("Your array is: ", LIST_1)
        NUMBER_2=int(input("Enter the number of elements of second list: "))
        LIST_2=[]
        for j in range(NUMBER_2):
            LIST_2.append(int(input()))
        print("Your array is: ", LIST_2)
        merge_list_and_sort(LIST_1,LIST_2)
    except Exception as e:
        print("Enter the valid input")
    