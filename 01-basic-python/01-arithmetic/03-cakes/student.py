# Write your code here
def cakes(eggs, butter, flour):
    eggCounter = eggs // 5
    butterCounter = butter // 250
    flourCounter = flour // 250
    return min(eggCounter, butterCounter, flourCounter)
