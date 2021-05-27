
import argparse
import re
import os

from PIL import Image

parser = argparse.ArgumentParser(prog='thumbnail')
parser.add_argument('files', default="*")
parser.add_argument('--size', default=r"64x64")
parser.add_argument('--pattern', default=r"%b-thumbnail.%x")

args = parser.parse_args()
wantedFiles = re.sub(r"\*", "", args.files)


files = []

for file in os.listdir("./"):
    if re.search(f"^{wantedFiles}", file):
        files.append(file)

x = re.fullmatch(r"(\d+)x(\d+)", args.size)
sizes = x.groups()
width = sizes[0]
height = sizes[1]
size = (int(width), int(height))

for file in files:
    filename = re.match(r"^(.+?)(\..+)", file)
    if filename:
        newfile = file
        name = filename.group(1)
        extension = filename.group(2)
        newfile.replace(r'%b', name).replace(r'.%x', extension)

        addition = re.match(".+?-(.+?)\..+", args.pattern)
        thumbname = addition.groups()[0]
        newfile = f"{name}-{thumbname}{extension}"

        image = Image.open(file)
        image.thumbnail(size)
        image.save(newfile)
