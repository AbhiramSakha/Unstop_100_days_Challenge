MOD = 10 ** 9 + 7

def user_logic(N, K, L, R):
    m = R - L + 1

    if K >= N:
        return 0

    # dp[max_rank][cost]
    dp = [[0] * N for _ in range(m)]

    # First element
    for first in range(m):
        dp[first][0] = 1

    # Process remaining positions
    for _ in range(1, N):
        ndp = [[0] * N for _ in range(m)]

        for mx in range(m):
            for cost in range(N):
                cur = dp[mx][cost]
                if cur == 0:
                    continue

                # Choose value <= current maximum
                ndp[mx][cost] = (ndp[mx][cost] + cur * (mx + 1)) % MOD

                # Choose new maximum
                if cost + 1 < N:
                    for newmx in range(mx + 1, m):
                        ndp[newmx][cost + 1] = (ndp[newmx][cost + 1] + cur) % MOD

        dp = ndp

    ans = 0
    for mx in range(m):
        for cost in range(K, N):
            ans = (ans + dp[mx][cost]) % MOD

    return ans


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    K = int(data[1])
    L = int(data[2])
    R = int(data[3])

    print(user_logic(N, K, L, R))

if __name__ == "__main__":
    main()