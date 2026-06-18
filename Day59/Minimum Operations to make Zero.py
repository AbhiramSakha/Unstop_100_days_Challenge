def minimum_operations_to_zero(n):
    ops = 0
    while n:
        ops ^= n
        n >>= 1

    if ops < 2:
        return 0

    sieve = [True] * (ops + 1)
    sieve[0] = sieve[1] = False

    p = 2
    while p * p <= ops:
        if sieve[p]:
            for j in range(p * p, ops + 1, p):
                sieve[j] = False
        p += 1

    return sum(sieve)


def main():
    import sys

    data = sys.stdin.read().split()

    # Use only the first integer
    n = int(data[0])

    print(minimum_operations_to_zero(n))


if __name__ == "__main__":
    main()