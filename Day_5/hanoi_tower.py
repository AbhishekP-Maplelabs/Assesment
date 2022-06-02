"""
    Description: To solve the hanoi tower puzzle
"""
def tower_of_hanoi(disks, source, auxiliary, target):
    """
        This function prints the steps to solve hanoi tower puzzle
    """
    if disks == 1:
        print(f"Move disk 1 from  {source} to  {target}.")
        return
    tower_of_hanoi(disks - 1, source, target, auxiliary)
    print(f"Move disk {disks} from  {source} to  {target}.")
    tower_of_hanoi(disks - 1, auxiliary, source, target)
if __name__=="__main__":
    try:
        DISKS = int(input('Enter the number of disks: '))
        tower_of_hanoi(DISKS, 'source rod', 'auxilary rod', 'target rod')
    except Exception as e:
        print("Enter the valid input")
