"""
    Description: To find the length of list using recursion.
"""
class Length:
    """
        has function to print the size of list.
    """
    def count(self, input_list):
        """
            function to find the length of list using recursion.
        """
        if len(input_list) == 0:
            return 0
        return 1 + self.count(input_list[1:])
def main():
    """
        main function that calls the function to find the length of list
    """
    item_list = input("Enter elements of the list: ").split(' ')
    obj = Length()
    length = obj.count(item_list)
    print("Length of List:", length)
if __name__ == "__main__":
    main()
