MOD = int(1e9 + 7)

def seat_allotment(n):
    if n % 2 == 1:
        return 0

    if n == 0:
        return 1
    if n == 2:
        return 3

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[2] = 3

    for i in range(4, n + 1, 2):
        dp[i] = (4 * dp[i - 2] - dp[i - 4]) % MOD

    return dp[n]

def main():
    import sys
    input = sys.stdin.read

    n = int(input().strip())

    result = seat_allotment(n)
    print(result)

if __name__ == "__main__":
    main()