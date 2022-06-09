"""
    Description: To implement heap sort
"""
def heapify(num_list, size, index):
    """
        To heapify subtree rooted at index.
    """
    largest = index
    left_root = 2 * index + 1
    right_root = 2 * index + 2
    if left_root < size and num_list[index] < num_list[left_root]:
        largest = left_root
    if right_root < size and num_list[largest] < num_list[right_root]:
        largest = right_root
    if largest != index:
        num_list[index], num_list[largest] = num_list[largest], num_list[index]
        heapify(num_list, size, largest)
def heap_sort(num_list):
    """
        Function to heap sort.
    """
    length = len(num_list)
    for num in range(length//2, -1, -1):
        heapify(num_list, length, num)
    for i in range(length-1, 0, -1):
        num_list[i], num_list[0] = num_list[0], num_list[i]
        heapify(num_list, i, 0)
if __name__ == "__main__":
    try:
        NUMBER=int(input("Enter the length of list: "))
        LIST=[]
        for element in range (NUMBER):
            LIST.append(int(input()))
        LENGTH = len(LIST)
        heap_sort(LIST)
        print("Sorted array is")
        print("Sorted list is: ")
        for result in range(LENGTH):
            print(LIST[result], end=' ')
    except ValueError as v:
        print("Enter valid input")
    except IndexError as I:
        print("enter numbers within range")
  