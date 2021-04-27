# Write your code here
import re
def remove_repeated_words(string):
    subbed = re.sub(r'([a-z]+)(\s\1)+',r'\1',string)
    #        re.sub(r'([a-z]+)( \1)+', r'\1', string)
    return subbed