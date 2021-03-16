import re
def contains_no_a(string):
    if re.fullmatch(r'[^a]*',string):
        return True
    return False
