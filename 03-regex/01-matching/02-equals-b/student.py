# Write your code here
import regex
def equals_b(string):
    if regex.fullmatch('b', string):
        return True
    return False
