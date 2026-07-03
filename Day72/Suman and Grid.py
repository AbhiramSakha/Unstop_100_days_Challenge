def main():
    import sys

    input = sys.stdin.readline

    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]

    dp = grid[0][:]

    for i in range(1, n):
        min1 = float('inf')
        min2 = float('inf')
        idx1 = -1

        # Find minimum and second minimum in previous row
        for j in range(n):
            if dp[j] < min1:
                min2 = min1
                min1 = dp[j]
                idx1 = j
            elif dp[j] < min2:
                min2 = dp[j]

        new_dp = [0] * n
        for j in range(n):
            if j == idx1:
                new_dp[j] = grid[i][j] + min2
            else:
                new_dp[j] = grid[i][j] + min1

        dp = new_dp

    print(min(dp))


if __name__ == "__main__":
    main()