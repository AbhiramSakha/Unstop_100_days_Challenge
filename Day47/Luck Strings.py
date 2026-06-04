def count_lucky_strings(N):
    MOD = 10**9 + 7

    if N == 1:
        return 2
    if N == 2:
        return 2

    a, b = 2, 2  # A1, A2

    for _ in range(3, N + 1):
        a, b = b, (a + b) % MOD

    return b


def main():
    import sys
    input = sys.stdin.read
    data = input().strip()

    N = int(data)

    result = count_lucky_strings(N)
    print(result)


if __name__ == "__main__":
    main()