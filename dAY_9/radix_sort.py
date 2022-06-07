"""
    Description: Implementation of radix sort
"""
def counting_sort(arr, digit_1):
    """
        Using counting sort to sort the list according to the significant place vlue.
    """
    length = len(arr)
    output = [0] * (length)
    count = [0] * (10)
    for num in range(0, length):
        index = arr[num] // digit_1
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = length - 1
    while i >= 0:
        index = arr[i] // digit_1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    j = 0
    for j in range(0, len(arr)):
        arr[j] = output[j]
def radix_sort(list_1):
    """
        Function for radix sort
    """
    max1 = max(list_1)
    digit = 1
    while max1 / digit > 1:
        counting_sort(list_1, digit)
        digit *= 10
NUMBER=int(input("enter the length of list: "))
LIST = []
for number in range(NUMBER):
    LIST.append(int(input()))
radix_sort(LIST)
for k in range(0,len(LIST)):
    print(LIST[k],end=" ")
