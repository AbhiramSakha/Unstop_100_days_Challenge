import sys
sys.setrecursionlimit(1 << 20)

def user_logic(n, edges):
    g = [[] for _ in range(n)]

    for u, v in edges:
        u -= 1
        v -= 1
        g[u].append(v)
        g[v].append(u)

    def check(K):
        ok = True
        dp = [0] * n
        typ = [0] * n

        def dfs(v, p):
            nonlocal ok

            leaf = True
            x0 = []
            x1 = []

            for to in g[v]:
                if to == p:
                    continue

                leaf = False
                dfs(to, v)

                if typ[to] == 0:
                    x0.append(dp[to])
                else:
                    x1.append(dp[to])

            if leaf:
                dp[v] = 1
                typ[v] = 1
                return

            x0.sort(reverse=True)
            x1.sort(reverse=True)

            if len(x1) <= 1:
                y = x0[:]
                for a in x1:
                    y.append(a - 1)

                y.sort(reverse=True)

                mx = y[0]

                if mx + 1 > K:
                    ok = False

                if len(y) >= 2 and y[0] + y[1] + 1 > K:
                    ok = False

                typ[v] = 1
                dp[v] = mx + 1

            else:
                x1a = x1[:]

                x1a[0] -= 1

                y = x0[:]
                y.extend(x1a)
                y.sort(reverse=True)

                cand = y[0] + 1

                if y[0] + 1 > K:
                    cand = 10 ** 9

                if len(y) >= 2 and y[0] + y[1] + 1 > K:
                    cand = 10 ** 9

                x1a[1] -= 1

                y = x0[:]
                y.extend(x1a)
                y.sort(reverse=True)

                if y[0] + 1 > K:
                    ok = False

                if len(y) >= 2 and y[0] + y[1] + 1 > K:
                    ok = False

                if y[0] + 1 < cand:
                    typ[v] = 0
                    dp[v] = y[0] + 1
                else:
                    typ[v] = 1
                    dp[v] = cand

        dfs(0, -1)
        return ok

    lo, hi = 1, n

    while lo < hi:
        mid = (lo + hi) // 2

        if check(mid):
            hi = mid
        else:
            lo = mid + 1

    return lo


def main():
    data = sys.stdin.buffer.read().split()

    n = int(data[0])

    edges = []
    idx = 1

    for _ in range(n - 1):
        u = int(data[idx])
        v = int(data[idx + 1])
        idx += 2
        edges.append((u, v))

    print(user_logic(n, edges))

if __name__ == "__main__":
    main()