def user_logic(n, weights):
    m = (1 << (n + 1)) - 1

    w = [0] * (m + 1)
    for i in range(2, m + 1):
        w[i] = weights[i - 2]

    ans = 0

    def dfs(v):
        nonlocal ans

        if 2 * v > m:
            return 0

        left = dfs(2 * v) + w[2 * v]
        right = dfs(2 * v + 1) + w[2 * v + 1]

        ans += abs(left - right)

        return max(left, right)

    dfs(1)
    return ans


def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))

    n = data[0]
    weights = data[1:]

    print(user_logic(n, weights))

if __name__ == "__main__":
    main()