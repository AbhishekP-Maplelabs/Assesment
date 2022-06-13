"""
    Description: URL is valid or not using regular expression
"""
import re
def is_valid_url(demo_url):
    """
        Function to validate the the URLs
    """
    regex = ("((http|https)://)(www.)?" +
			"[a-zA-Z0-9@:%._\\+~#?&//=]" +
			"{2,256}\\.[a-z]" +
			"{2,6}\\b([-a-zA-Z0-9@:%" +
			"._\\+~#?&//=]*)")
    string = re.compile(regex)
    if str is None:
        return False
    if re.search(string, demo_url):
        return True
    return False
if __name__ == "__main__":
    try:
        DEMO_URL = input("Enter the url: ")
        if is_valid_url(DEMO_URL) :
            print("Yes")
        else:
            print("No")
    except ValueError as e :
        print("Enter valid input")
    except TypeError as t:
        print("enter proper value")
