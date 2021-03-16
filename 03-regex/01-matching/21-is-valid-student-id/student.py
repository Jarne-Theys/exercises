import re
def is_valid_student_id(string):
    if re.fullmatch('[srSR]\d{7}',string):
        return True
    return False