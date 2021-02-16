# Write your code here
def remove_duplicates(xs):
    algehad = set()
    result = []
    for x in xs:
        if x not in algehad:
            result.append(x)
            algehad.add(x)
    return result
    # return list(dict.fromkeys(xs)) Kortere oplossing?
