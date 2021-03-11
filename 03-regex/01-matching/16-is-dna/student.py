# Write your code here
import re
def is_dna(string):
    if re.fullmatch('[GATC]*',string):
        return True
    return False