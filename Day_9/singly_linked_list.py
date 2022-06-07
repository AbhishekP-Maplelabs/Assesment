"""
    Decription: Implementation of singly linked list operations
"""
class Node:
    """
    Creation of node
    """
    def __init__(self, input_data):
        """
            Function to create the node
        """
        self.data = input_data
        self.next = None
class LinkedList:
    """
        Creation of linked list.
    """
    def __init__(self):
        """
        Function to create the linked list
        """
        self.head = None
    def get_node(self, node_index):
        """
        Function to get the node
        """
        current = self.head
        for i in range(node_index):
            if current is None:
                return None
            current = current.next
        return current
    def get_prev_node(self, prev_ref_node):
        """
        Function to get previous node
        """
        current = self.head
        while (current and current.next != prev_ref_node):
            current = current.next
        return current
    def insert_after(self, input_node, after_ref_node):
        """
        Function to insert element after the specified node
        """
        new_node.next = input_node.next
        input_node.next = after_ref_node
    def insert_before(self, prior_node, before_ref_node):
        """
        Function to insert element before the specified node
        """
        prev_node = self.get_prev_node(prior_node)
        self.insert_after(prev_node, before_ref_node)
    def insert_at_beg(self, start_node):
        """
        Function to insert elementat the begining of the list
        """
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = start_node
    def insert_at_end(self, end_node):
        """
        Function to insert the element at the end of the list
        """
        if self.head is None:
            self.head = end_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def remove(self, remove_node):
        """
        Function to remove the element from the list
        """
        prev_node = self.get_prev_node(remove_node)
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = node.next
    def display(self):
        """
        Function to display the elements in the list
        """
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
a_llist = LinkedList()
print('Menu')
print('insert <data> after <index>')
print('insert <data> before <index>')
print('insert <data> at beg')
print('insert <data> at end')
print('remove <index>')
print('quit')
while True:
    print('The list: ', end = '')
    a_llist.display()
    print()
    do = input('What would you like to do? ').split()
    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        position = do[3].strip().lower()
        new_node = Node(data)
        suboperation = do[2].strip().lower()
        if suboperation == 'at':
            if position == 'beg':
                a_llist.insert_at_beg(new_node)
            elif position == 'end':
                a_llist.insert_at_end(new_node)
        else:
            index = int(position)
            ref_node = a_llist.get_node(index)
            if ref_node is None:
                print('No such index.')
                continue
            if suboperation == 'after':
                a_llist.insert_after(ref_node, new_node)
            elif suboperation == 'before':
                a_llist.insert_before(ref_node, new_node)
    elif operation == 'remove':
        index = int(do[1])
        node = a_llist.get_node(index)
        if node is None:
            print('No such index.')
            continue
        a_llist.remove(node)
    elif operation == 'quit':
        break
