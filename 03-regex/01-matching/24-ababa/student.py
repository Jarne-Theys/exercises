import re
def ababa(string):
    if re.fullmatch(r'(.+)(.+)\1\2\1',string):
        return True
    return False
