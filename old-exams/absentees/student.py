result = open("absentees.txt", "w")
with open(r"C:\Users\Jarne Theys\Desktop\Scripttalen\exercises\old-exams\absentees\attending.txt") as attendees:
    with open(r"C:\Users\Jarne Theys\Desktop\Scripttalen\exercises\old-exams\absentees\all.txt") as all:
        allNextLine = all.readline().lower()
        attNextLine = attendees.readline().lower()
        while attNextLine:
            allNextLine = allNextLine.replace('\n', '')
            attNextLine = attNextLine.replace('\n', '')
            if allNextLine != attNextLine:
                result.write(f"{allNextLine}\n")
                allNextLine = all.readline().lower()
            if allNextLine == attNextLine:
                if allNextLine == '':
                    break
                allNextLine = all.readline().lower()
                attNextLine = attendees.readline().lower()
        while allNextLine:
            allNextLine = allNextLine.replace('\n', '')
            result.write(f"{allNextLine}\n")
            allNextLine = all.readline().lower()
