# Write your code here
import re
def only_letters(string):
    if re.fullmatch('[a-z | A-Z]*',string):
        return True
    return False