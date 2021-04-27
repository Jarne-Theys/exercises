import re
def thrice_repeated(string):
    if re.fullmatch(r'(.+)\1\1',string):
        return True
    return False
