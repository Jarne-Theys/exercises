# Write your code here
def by_length(string):
    return len(string)


def longest_string(strings):
    return max(strings, key=by_length)
