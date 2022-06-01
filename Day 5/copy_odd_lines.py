"""
    Description: To read contents of a file and copy only the content of odd lines into new file.
"""
try:
    file = open('file.txt', 'r')
    new_file = open('file_1.txt', 'w')
    count = file.readlines()
    for i in range(0, len(count)):
        if i % 2 == 0:
            new_file.write(count[i])
        else:
            pass
    new_file.close()
    new_file = open('file_1.txt', 'r')
    count1 = new_file.read()
    print(count1)
    file.close()
    new_file.close()
except Exception as e:
    print("Enter valid input")
