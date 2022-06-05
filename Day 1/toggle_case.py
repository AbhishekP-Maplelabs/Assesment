"""
description: To toggle the charecters in the string
"""
import re
def toggle_case(word):
    """
    this function will interchange the case of the charecters in the string.
    """
    regex = re.compile('[@_!#$%^&*()<>?//|}{~:]')
    if regex.search(word) is None:
        string_1 = str()
        for i in word:
            if i.isupper():
                i = i.lower()
                string_1 = string_1 + i
            else:
                i = i.upper()
                string_1 = string_1 + i
    return string_1
if __name__ == "__main__":
    try:
        STRING=input("Please enter the string: ")
        result=toggle_case(STRING)
        print(STRING+"after changing the case is: "+result)
    except Exception as e:
        print("Please enter the proper string ")
