def water_jug(X, i, j):
    dp = [[0.0] * (r + 1) for r in range(i + 1)]
    dp[1][1] = X

    for r in range(1, i):
        for c in range(1, r + 1):
            overflow = max(0.0, dp[r][c] - 1.0)
            if overflow > 0:
                dp[r][c] = 1.0
                dp[r + 1][c] += overflow / 2.0
                dp[r + 1][c + 1] += overflow / 2.0

    return min(1.0, dp[i][j])

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    i = int(data[0])
    j = int(data[1])
    X = float(data[2])

    result = water_jug(X, i, j)
    print(f"{result:.6f}")

if __name__ == "__main__":
    main()