# Write your code here
def card_value(string):
    if type(string) is int:
        return string
    elif string == "Jack":
        return 11
    elif string == "Queen":
        return 12
    elif string == "King":
        return 13
    elif string == "Ace":
        return 1
