"""
    Description:To find the mirror characters in the string
"""
def compute(string, position):
    """
        This function prints the mirror characters in the string from the given position
    """
    reverse_alphabet = "zyxwvutsrqponmlkjihgfedcba"
    length = len(string)
    answer = ""
    for i in range(0, position):
        answer = answer + string[i]
    for i in range(position, length):
        answer = (answer + reverse_alphabet[ord(string[i]) - ord('a')])
    return answer
try:
    STRING = input("Enter the string: ")
    POSITION = int(input("Enter the position to be mirrored: "))
    if POSITION>len(STRING):
        print("Enter the valid position")
        quit()
    ANSWER = compute(STRING, POSITION - 1)
    print(f"String after mirroring the characters from entered position is: {ANSWER}")
except Exception as e:
    print("Enter proper string")
