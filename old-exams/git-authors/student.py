import re
outputset = []
with open("input.txt", "r") as input:
    with open("output.txt", "w") as output:
        for line in input:
            search = re.search("Author: (.+?) <", line)
            if search:
                outputset.append(search.group(1))
        result = sorted(set(outputset))
        for element in result:
            output.write(element + "\n")
