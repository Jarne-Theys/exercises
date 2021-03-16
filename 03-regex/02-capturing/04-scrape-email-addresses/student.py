# Write your code here
# re.fullmatch(r'[a-z0-9.]+@(student\.)?ucll\.be',string)
import re
def scrape_email_addresses(string):
    list = re.findall(r'([\w\d.]+@[\w.]+)',string)
    return list
