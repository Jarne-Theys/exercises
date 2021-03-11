# Write your code here
import re
def contains_three_digits(string):
    if re.fullmatch('.*\d.*\d.*\d.*',string):
        return True
    return False