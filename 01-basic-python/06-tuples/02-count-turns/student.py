# Write your code here
<<<<<<< HEAD
def count_turns(xs):
    result = 0
    for (x, y, z) in zip(xs, xs[1:], xs[2:]):
        if x < y > z or x > y < z:
            result += 1
    return result
=======
def count_turns(ns):
    counter = 0
    for (x, y) in zip(ns, ns[1:]):
        if counter % 2 == 0 and x > y:
            counter += 1
        if counter % 2 != 0 and x < y:
            counter += 1
    return counter
>>>>>>> 10d21465ad33b592b28f8bf251e88891467322dd
