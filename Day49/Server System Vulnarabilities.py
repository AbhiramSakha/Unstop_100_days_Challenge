def user_logic(N, K, arr):
    dp = [0] + [float('inf')] * N

    for i in range(1, N + 1):
        mx = 0
        for j in range(i, max(0, i - K), -1):
            mx = max(mx, arr[j - 1])
            dp[i] = min(dp[i], dp[j - 1] + mx)

    return dp[N]

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])
    K = int(data[1])
    arr = list(map(int, data[2:]))

    result = user_logic(N, K, arr)
    print(result)

if __name__ == "__main__":
    main()