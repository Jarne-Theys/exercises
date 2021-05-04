import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as webpage:
    content = webpage.read()

print(content)
