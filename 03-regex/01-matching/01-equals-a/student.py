# Write your code here
import regex
def equals_a(string):
    if regex.fullmatch('a', string):
        return True
    return False