# Write your code here
import re
def abc_or_xyz(string):
    if re.fullmatch('abc|xyz',string):
        return True
    return False