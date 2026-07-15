def mod_inverse(A, M):
    A %= M
    return pow(A, M - 2, M)


def solve(n):
    return n > 0 and (n & (n - 1)) == 0


def main():
    import sys
    input = sys.stdin.read
    data = input().strip()

    n = int(data)

    t = mod_inverse(n, 10007)

    print(1 if solve(t) else 0)


if __name__ == "__main__":
    main()