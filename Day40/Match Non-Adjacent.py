MOD = 998244353

def user_logic(N, M, K):
    if K > N * M:
        K = N * M

    dp = [0] * (K + 1)
    dp[0] = 1

    for _ in range(N):
        new_dp = [0] * (K + 1)

        window = 0
        for s in range(K + 1):
            window = (window + dp[s]) % MOD

            if s - M - 1 >= 0:
                window = (window - dp[s - M - 1]) % MOD

            new_dp[s] = window

        dp = new_dp

    return sum(dp) % MOD


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    N = int(data[0])
    M = int(data[1])
    K = int(data[2])

    result = user_logic(N, M, K)
    print(result)

if __name__ == "__main__":
    main()