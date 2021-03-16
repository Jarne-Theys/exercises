import re
def twice_repeated(string):
    if re.fullmatch(r'(.)\1',string):
        return True
    return False