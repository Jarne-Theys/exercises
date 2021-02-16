# Write your code here
def by_length(string):
    return len(string)


def nth_longest_string(n, strings):
    result = sorted(strings, key=by_length)
    return result[-n]
