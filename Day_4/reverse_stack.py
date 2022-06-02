"""
    Description: To reverse the stack using recursion.
"""
class Stack:
    """
        create class of stack
    """
    def __init__(self):
        """
            create empty list
        """
        self.elements = []
    def push(self, value):
        """
        push() to insert an element
        """
        self.elements.append(value)
    def pop(self):
        """
        pop() to remove an element
        """
        return self.elements.pop()
    def empty(self):
        """
        empty() check the stack is empty of not
        """
        return not self.elements
    def display(self):
        """
        show() display stack
        """
        for value in reversed(self.elements):
            print(value)
def bottom_insert(stack, value):
    """
        Insert_Bottom() insert value at bottom
    """
    if stack.empty():
        stack.push(value)
    else:
        popped = stack.pop()
        bottom_insert(stack, value)
        stack.push(popped)
def reverse(stack):
    """
        reverse the stack
    """
    if stack.empty():
        pass
    else:
        popped = stack.pop()
        reverse(stack)
        bottom_insert(stack, popped)
if __name__=="__main__":
    STACK = Stack()
    data_list = input('Please enter the elements to push: ').split()
    for data in data_list:
        STACK.push(int(data))
    print("Original Stack")
    STACK.display()
    print("\nStack after Reversing")
    reverse(STACK)
    STACK.display()
