# open file in read mode
file = open('file.txt', 'r')

# open other file in write mode
new_file = open('file_1.txt', 'w')

# read the content of the file line by line
count = file.readlines()
type(count)
for i in range(0, len(count)):
    if i % 2 == 0:
        new_file.write(count[i])
    else:
        pass

# close the file
new_file.close()

# open file in read mode
new_file = open('file_1.txt', 'r')

# read the content of the file
count1 = new_file.read()

# print the content of the file
print(count1)

# close all files
file.close()
new_file.close()
