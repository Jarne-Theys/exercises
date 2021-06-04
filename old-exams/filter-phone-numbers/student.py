import re
with open("output.txt", "w") as output:
    with open("input.txt", "r") as input:
        for line in input:
            if re.fullmatch(r"(\+32\-|0)4[5-9]\d\-[\d]{2}\-[\d]{2}\-[\d]{2}", line.strip()):
                output.write(line)
