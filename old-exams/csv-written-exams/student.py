import csv


with open(r"C:\Users\Jarne Theys\Desktop\Scripttalen\exercises\old-exams\csv-written-exams\exam-schedule.csv") as file:
    with open('output.txt', 'w') as out:
        data = csv.DictReader(file)

        result = {}

        for row in data:
            if row['Ex. Soortx'] == 'S':
                ids = row['Lector'].split('/')

                for id in ids:
                    result[id] = result.get(id, 0) + 1

        result = sorted(result.items())

        for id, count in result:
            out.write(f"{id} {count}\n")
