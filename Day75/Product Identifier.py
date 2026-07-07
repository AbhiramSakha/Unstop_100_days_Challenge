def user_logic(N, K):
    memo = {}

    def dfs(x):
        if len(str(x)) == N:
            return 0
        if len(str(x)) > N:
            return 10 ** 9

        if x in memo:
            return memo[x]

        ans = 10 ** 9

        for ch in str(x):
            d = ord(ch) - ord('0')
            if d >= 2:
                ans = min(ans, 1 + dfs(x * d))

        memo[x] = ans
        return ans

    ans = dfs(K)
    return -1 if ans == 10 ** 9 else ans




def main():
    import sys
    data = sys.stdin.read().split()
    N = int(data[0])
    K = int(data[1])
    print(user_logic(N, K))

if __name__ == "__main__":
    main()