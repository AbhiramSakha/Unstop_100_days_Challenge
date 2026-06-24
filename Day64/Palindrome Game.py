def min_insertions_to_palindrome(s):
    n = len(s)

    dp = [[0] * n for _ in range(n)]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] if length > 2 else 0
            else:
                dp[i][j] = 1 + min(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]

def main():
    import sys
    input = sys.stdin.read
    s = input().strip()

    result = min_insertions_to_palindrome(s)
    print(result)

if __name__ == "__main__":
    main()