# Write your code here
def format_time(h, m, s):
    hour = str(h).rjust(2, "0")
    minute = str(m).rjust(2, "0")
    second = str(s).rjust(2, "0")
    return f"{hour}:{minute}:{second}"