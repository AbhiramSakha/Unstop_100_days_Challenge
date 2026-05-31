def user_logic(n):
    MOD = 10**9 + 7

    if n == 0:
        return 2
    if n == 1:
        return 1

    a, b = 2, 1

    for _ in range(2, n + 1):
        a, b = b, (a + b) % MOD

    return b

def main():
    import sys
    input = sys.stdin.read
    data = input().strip()

    n = int(data)

    result = user_logic(n)
    print(result)

if __name__ == "__main__":
    main()