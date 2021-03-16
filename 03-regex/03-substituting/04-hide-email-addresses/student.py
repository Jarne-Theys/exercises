# Write your code here
import re
def hide_email_addresses(string):
    def replace_with_asterisk(match):
        return len(match.group(0))*"*"

    return re.sub(r'([\w\d.]+@[\w.]+)',replace_with_asterisk,string)