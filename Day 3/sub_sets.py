"""
    Description: To find all the possible subsets of distinct integers given in list.
"""
class GetSubset:
    """
        To get the possible subsets from distinct numbers given by user
    """
    def sort_list(self, my_list):
        """
            This function will sort the list before creating the subsets.
        """
        return self. subset_find([], sorted(my_list))
    def subset_find(self, curr, my_list):
        """
        This function returns all the possible subsets.
        """
        if my_list:
            return self. subset_find(curr, my_list[1:]) + self. subset_find(curr + [my_list[0]], my_list[1:])
        return [curr]
try:
    my_list = []
    NUMBER = int(input("Enter the number of elements in the list: "))
    for i in range(0,NUMBER):
        elem=int(input())
        my_list.append(elem)
    print("Subsets of the list are : ")
    print(GetSubset().sort_list(my_list))
except Exception as e:
    print("Enter valid input")
