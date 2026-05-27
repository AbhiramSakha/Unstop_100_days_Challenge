def user_logic(grid):
    """
    Find minimum path sum from top-left to bottom-right.
    Only right and down moves are allowed.
    """

    n = len(grid)
    m = len(grid[0])

    dp = [[0] * m for _ in range(n)]

    dp[0][0] = grid[0][0]

    # First row
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + grid[0][j]

    # First column
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + grid[i][0]

    # Fill remaining cells
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]

    return dp[n - 1][m - 1]


def main():
    import sys

    data = list(map(int, sys.stdin.read().strip().split()))

    n = data[0]
    m = data[1]

    grid = []
    idx = 2

    for _ in range(n):
        row = data[idx:idx + m]
        grid.append(row)
        idx += m

    print(user_logic(grid))


if __name__ == "__main__":
    main()