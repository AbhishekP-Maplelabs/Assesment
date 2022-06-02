"""
    Description: To extract the ip adress from the text file
"""
import re
try:
    with open('file_2.txt',encoding="utf8") as file:
        fstring = file.readlines()
    pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    LIST=[]
    for line in fstring:
        LIST.append(pattern.search(line)[0])
    print(f"The ip adresses are: {LIST}")
except FileNotFoundError as e:
    print("Enter valid input")
