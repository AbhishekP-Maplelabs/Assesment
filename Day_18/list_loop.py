"""Python program to  loop in the linked list
"""
class Node:
    """
        Constructor to initialize the node object.
    """
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    """
    Function to initialize head
    """
    def __init__(self):
        self.head = None
    def push(self, new_data):
        """
            Function to insert new node at the begining
        """
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def print_list(self):
        """
            Function to print the list.
        """
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
    def detect_loop(self):
        """
            Function to check for the loop
        """
        num_set = set()
        temp = self.head
        while temp:
            if temp in num_set:
                return True
            num_set.add(temp)
            temp = temp.next
        return False
if __name__ == "__main__":
    NUMBER=int(input("Enter the length of list: "))
    linked_list = LinkedList()
    print("push the numbers")
    for num in range(NUMBER):
        linked_list.push(int(input()))
linked_list.head.next = linked_list.head
if linked_list.detect_loop():
    print("Loop found")
else:
    print("No Loop ")
