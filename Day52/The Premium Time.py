def find_smallest_premium_prime(n):
    def is_prime(x):
        if x < 2:
            return False
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        i = 3
        while i * i <= x:
            if x % i == 0:
                return False
            i += 2
        return True

    p = 2
    while p <= n:
        if is_prime(p) and is_prime(n // p):
            return p

        if p == 2:
            p = 3
        else:
            p += 2

    return -1


def main():
    import sys
    input = sys.stdin.read
    n = int(input().strip())

    result = find_smallest_premium_prime(n)
    print(result)


if __name__ == "__main__":
    main()