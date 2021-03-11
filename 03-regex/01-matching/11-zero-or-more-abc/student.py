# Write your code here
import re
def zero_or_more_abc(string):
    if re.fullmatch('(abc)*',string):
        return True
    return False