def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def user_logic(s):
    # dp[c] = maximum valid subsequence ending with character c
    dp = [0] * 26

    for ch in s:
        x = ord(ch) - ord('a')
        best = 1

        if x >= 2:
            best = max(best, dp[x - 2] + 1)
        if x + 2 < 26:
            best = max(best, dp[x + 2] + 1)

        dp[x] = max(dp[x], best)

    ans = max(dp)
    if ans == 1:
        return 0
    return ans


def main():
    import sys
    s = sys.stdin.read().strip()

    max_length = user_logic(s)
    result = 1 if is_prime(max_length) else 0
    print(result)


if __name__ == "__main__":
    main()