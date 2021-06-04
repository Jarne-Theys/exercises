import argparse
import os
import re
import math
from os import walk


parser = argparse.ArgumentParser(prog='find')
parser.add_argument("files")
parser.add_argument("--minimum-size", type=int, default=0)
parser.add_argument("--maximum-size", type=int, default=math.inf)
parser.add_argument("-no-directories", action="store_false")
parser.add_argument("-no-files", action="store_false")
parser.add_argument("--extension", default=".*")
parser.add_argument("--contains", default=".*")
args = parser.parse_args()

inclFiles = args.no_files
inclDirs = args.no_directories

dirs = []
files = []


#path = r"C:\Users\Jarne Theys\Desktop\Scripttalen\exercises\04-scripting\03-argparse\03-find"
path = args.files


for (dirpath, dirnames, filenames) in walk(path, topdown=True):
    if inclFiles:
        for name in filenames:
            try:
                if re.fullmatch(f".+?{args.extension}$", name) and os.path.getsize(name) < args.maximum_size and os.path.getsize(name) > args.minimum_size and re.fullmatch(args.contains, name):
                    files.append(name)
            except FileNotFoundError as error:
                print(f"Er is een fout opgetreden bij het lezen van {name}!")
    if inclDirs:
        for name in dirnames:
            dirs.append(name)

print("DIRECTORIES:")
print(dirs)
print("\nFILES:")
print(files)
print("\nPATH:")
print(path)
