def determine_winner(n, balls):
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = balls[i]

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = max(
                balls[i] - dp[i + 1][j],
                balls[j] - dp[i][j - 1]
            )

    return "Aryan" if dp[0][n - 1] >= 0 else "Ankit"

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    balls = list(map(int, data[1:]))

    result = determine_winner(n, balls)
    print(result)

if __name__ == "__main__":
    main()