"""
    Description: To extract the ip adress from the text file
"""
import re
with open('D:/Work/Practice/module_1/Module_2/assesment/Day 5/file_2.txt') as file:
    fstring = file.readlines()
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
LIST=[]
for line in fstring:
    LIST.append(pattern.search(line)[0])
print(f"The ip adresses are: {LIST}")
