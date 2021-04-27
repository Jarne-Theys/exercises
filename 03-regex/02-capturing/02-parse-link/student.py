# Write your code here
#<a href="xxx">lalala</a>
import re
def parse_link(string):
    match = re.fullmatch(r'<a href="(.+)">(.+)</a>',string)
    if match:
        link, tekst = match.groups()
        return tuple([tekst,link])
