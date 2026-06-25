def count_filo_ways(n):
    while n % 2 == 0:
        n //= 2

    ways = 1
    p = 3

    while p * p <= n:
        exp = 0
        while n % p == 0:
            exp += 1
            n //= p
        ways *= (exp + 1)
        p += 2

    if n > 1:
        ways *= 2

    return ways

if __name__ == "__main__":
    n = int(input())
    result = count_filo_ways(n)
    print(result)