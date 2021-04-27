import re
def is_valid_time(string):
    return re.fullmatch(r'\d\d\:\d\d\:\d\d(\.\d\d\d)*',string)
