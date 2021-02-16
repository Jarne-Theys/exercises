# Write your code here
def slug(name):
    delen = name.split(' ')
    voornaam = delen[0]
    achternaam = delen[1:]

    return '-'.join(char.lower() for char in achternaam + [voornaam])
