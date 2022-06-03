"""
    To parse and process the URL.
"""
import re
def parsing_url(url):
    """
        Function returns the host name and Protocol from URL using regex
    """
    obj1 = re.findall('(\\w+)://',url)
    print(f"Protocol: {obj1}")
    obj2 = re.findall('://www.([\\w\\-\\.]+)',url)
    print(f"Host name: {obj2}")
if __name__ == "__main__":
    try:
        DEMO_URL = 'https://www.maplelabs.com/'
        parsing_url(DEMO_URL)
    except Exception as e:
        print("Enter valid input")
