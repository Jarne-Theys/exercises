# Write your code here
# Niet gelukt
def format_grades(grades):

    def gemiddelde(ns):
        return round(sum(ns) / len(ns))

    return "\n".join(f'{name}: {gemiddelde(grades)}' for name, grades in grades.items())
