def longest_palindromic_subsequence(s):
    n = len(s)

    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j]:
                if length == 2:
                    dp[i][j] = 2
                else:
                    dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]


def main():
    import sys
    input = sys.stdin.read
    s = input().strip()

    result = longest_palindromic_subsequence(s)
    print(result)


if __name__ == "__main__":
    main()