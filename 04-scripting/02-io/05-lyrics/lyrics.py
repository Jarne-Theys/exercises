import sys
import json
import urllib.request

artist = sys.argv[1]
song = sys.argv[2]

url = f"https://api.lyrics.ovh/v1/{artist}/{song}".replace(' ', '%20')

with urllib.request.urlopen(url) as webpage:
    obj = json.loads(webpage.read())
print(obj["lyrics"])
