"""
    Description: To find all the possible subsets of distinct integers given in list.
"""
class GetSubset:
    """
        To get the possible subsets from distinct numbers given by user
    """
    def sort_list(self, num_list):
        """
            This function will sort the list before creating the subsets.
        """
        return self. subset([], sorted(num_list))
    def subset(self, curr, num_list):
        """
        This function returns all the possible subsets.
        """
        if num_list:
            return self.subset(curr,num_list[1:])+self.subset(curr+[num_list[0]],num_list[1:])
        return [curr]
if __name__ == "__main__":
    try:
        my_list = []
        NUMBER = int(input("Enter the number of elements in the list: "))
        for i in range(0,NUMBER):
            elem=int(input())
            my_list.append(elem)
        print("Subsets of the list are : ")
        OBJECT=GetSubset()
        print(OBJECT.sort_list(my_list))
    except Exception as e:
        print("Enter valid input")
