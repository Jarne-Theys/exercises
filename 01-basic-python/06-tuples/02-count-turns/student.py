# Write your code here
def count_turns(ns):
    counter = 0
    for (x, y) in zip(ns, ns[1:]):
        if counter % 2 == 0 and x > y:
            counter += 1
        if counter % 2 != 0 and x < y:
            counter += 1
    return counter
