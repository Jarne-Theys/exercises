# Write your code here
def is_prime(n):
    for x in range(2, n):
        if n % x == 0:
            return False
    return n > 1