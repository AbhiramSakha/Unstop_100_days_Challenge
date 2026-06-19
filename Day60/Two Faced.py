def user_logic(n, P, Q):
    MOD = 998244353

    pos = [0] * (n + 1)
    for i, x in enumerate(P):
        pos[x] = i

    perm = [0] * (n + 1)
    for x in range(1, n + 1):
        perm[x] = Q[pos[x]]

    fib = [0] * (n + 2)
    fib[1] = 1
    for i in range(2, n + 2):
        fib[i] = (fib[i - 1] + fib[i - 2]) % MOD

    visited = [False] * (n + 1)
    ans = 1

    for v in range(1, n + 1):
        if not visited[v]:
            cur = v
            length = 0

            while not visited[cur]:
                visited[cur] = True
                cur = perm[cur]
                length += 1

            if length == 1:
                ways = 1
            else:
                ways = (fib[length - 1] + fib[length + 1]) % MOD

            ans = (ans * ways) % MOD

    return ans


def main():
    import sys
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    P = list(map(int, data[1:n + 1]))
    Q = list(map(int, data[n + 1:2 * n + 1]))

    print(user_logic(n, P, Q))

if __name__ == "__main__":
    main()