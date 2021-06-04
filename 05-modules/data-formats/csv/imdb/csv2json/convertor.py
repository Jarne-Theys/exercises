import csv
import argparse

parser = argparse.ArgumentParser(prog="convert")
parser.add_argument("file")
args = parser.parse_args()
file = args.file

jsonArray = []

with open(file) as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        jsonArray.append(row)
print(jsonArray)
