"""
    Description: To print the list of items greater than average.
"""
def greater_than_avg(num_list,average):
    """
        Function to print the list of items greater than average.
    """
    list_1=[]
    for number,j in enumerate(num_list):
        if num_list[number]>average:
            list_1.append(num_list[number])
        else:
            j+=1
    print(f"list of items greater than average is: {list_1}")
if __name__ == "__main__":
    try:
        NUMBER=int(input("Enter the length of list: "))
        LIST=[]
        print("Enter the numbers: ")
        for i in range(NUMBER):
            LIST.append(int(input()))
        SUM=0
        for num,i in enumerate(LIST):
            SUM=SUM+LIST[num]
        AVERAGE=SUM//NUMBER
        greater_than_avg(LIST,AVERAGE)
    except ValueError as v:
        print("Enter valid input")
    except IndexError as i:
        print("Enter proper value")
