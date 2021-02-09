# Write your code here
def contains_duplicates(xs):
    xs = sorted(xs)
    previous = 99
    for x in xs:
        if x == previous:
            return True
        previous = x
    return False