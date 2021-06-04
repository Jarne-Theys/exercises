import re
result = {}
with open("input.txt", "r") as input:
    for line in input:
        search = re.search("Author: (.+?) <", line)
        if search:
            author = search.group(1)
            count = result.get(author, 0) + 1
            result[author] = count

result = sorted(result.items(), key=lambda x: x[1], reverse=True)
with open("output.txt", "w") as output:
    for key, value in result:
        output.write(key + ": " + str(value) + "\n")
