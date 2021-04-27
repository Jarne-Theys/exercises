# Write your code here
import re
def is_number(string):
    if re.fullmatch('\d+(\.\d+)?',string):
        return True
    return False