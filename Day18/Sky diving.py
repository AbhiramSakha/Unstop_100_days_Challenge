def min_parachutes(k, n):
    if n == 0 or k == 0:
        return 0

    dp = [[0] * (n + 1) for _ in range(k + 1)]
    
    m = 0
    while dp[k][m] < n:
        m += 1
        for i in range(1, k + 1):
            dp[i][m] = dp[i][m - 1] + dp[i - 1][m - 1] + 1
    return m

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # Number of floors
    k = int(data[1])  # Number of parachutes
    
    # Call user logic function and print the output
    result = min_parachutes(k, n)
    print(result)

if __name__ == "__main__":
    main()