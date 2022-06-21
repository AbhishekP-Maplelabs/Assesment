"""
    Description: Program to validate ip adress.
"""
def validate_adress(adress):
    """
        Function to validate ip adress;
    """
	# check number of periods
    if adress.count('.') != 3:
        return 'Invalid Ip address'
    adress_list = list(map(str, adress.split('.')))
	# check range of each number between periods
    for ele in adress_list:
        if int(ele) < 0 or int(ele) > 255 or (ele[0]=='0' and len(ele)!=1):
            return 'Invalid Ip address'
    return 'Valid Ip address'
ADRESS=input("Enter the ip adress: ")
RESULT=validate_adress(ADRESS)
print(RESULT)
