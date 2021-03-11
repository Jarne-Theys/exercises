# Write your code here
import re
def only_digits(string):
    if re.fullmatch('(\d)*',string):
        return True
    return False