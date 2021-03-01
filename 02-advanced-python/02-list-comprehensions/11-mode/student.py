# Write your code here
def mode(ns):
    result = {}
    for n in ns:
        if n not in result:
            result[n]=0
        result[n]+=1
    return(max(result,key=result.get))
