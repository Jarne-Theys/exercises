# Write your code here
# niet gelukt
def is_increasing(ns):
    # return all([zip(ns[:-1], ns[1:])])
    return all([x <= y for x, y in zip(ns, ns[1:])])
