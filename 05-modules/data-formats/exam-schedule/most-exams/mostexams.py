import csv
from collections import Counter

file = r"C:\Users\Jarne Theys\Desktop\Scripttalen\exercises\05-modules\data-formats\exam-schedule\exam-schedule.csv"

jsonArray = []

with open(file) as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        jsonArray.append(row)

count = Counter(player['Student ID'] for player in jsonArray)
result = str(count.most_common(1))
print(result[2:16].replace("'", "").replace(",", ":"))
