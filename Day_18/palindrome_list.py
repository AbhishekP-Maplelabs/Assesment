"""
    Description : Program to check for palindrome list.
"""
class Node:
    """
        Creating class node.
    """
    def __init__(self, input_value):
        """
            Initialization of linked list
        """
        self.data = input_value
        self.next = None
class LinkedList:
    """
        class linked list
    """
    def __init__(self):
        """
            creating the linked list
        """
        self.head = None
        self.last_node = None
    def append(self, data):
        """
            Function to append the data in the linked list
        """
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    def get_prev_node(self, ref_node):
        """
            Function to get the precious node.
        """
        current = self.head
        while (current and current.next != ref_node):
            current = current.next
        return current
def is_palindrome(llist):
    """
        Function to check for palindrome
    """
    start = llist.head
    end = llist.last_node
    while start not in (end,end.next):
        if start.data != end.data:
            return False
        start = start.next
        end = llist.get_prev_node(end)
    return True
num_list = LinkedList()
if __name__ == "__main__":
    try:
        data_list = input('Please enter the elements in the linked list: ').split()
        for number in data_list:
            num_list.append(int(number))
        if is_palindrome(num_list):
            print('The linked list is palindromic.')
        else:
            print('The linked list is not palindromic.')
    except ValueError as v:
        print("Enter valid input")
