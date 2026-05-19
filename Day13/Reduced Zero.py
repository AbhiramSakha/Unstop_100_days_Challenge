import math

def smallest_prime_factor(n):
    if n % 2 == 0:
        return 2
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return i
    return n  # n is prime

def user_logic(n):
    count = 0
    while n > 0:
        spf = smallest_prime_factor(n)
        n -= spf
        count += 1
    return count

n = int(input())
result = user_logic(n)
print(result)