from collections import deque

def count_removable_vertices(n, edges):
    """
    Write your logic here.
    Parameters:
        n (int): Number of vertices in the tree
        edges (list of tuple): List of edges
    Returns:
        int
    """

    graph = [[] for _ in range(n + 1)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    parent = [0] * (n + 1)
    order = []

    # BFS to get parent and traversal order
    q = deque([1])
    parent[1] = -1

    while q:
        node = q.popleft()
        order.append(node)

        for nei in graph[node]:
            if parent[nei] == 0:
                parent[nei] = node
                q.append(nei)

    # dp0[u] = max matching in subtree u when u is NOT matched to child
    # dp1[u] = max matching in subtree u when u IS matched to one child
    dp0 = [0] * (n + 1)
    dp1 = [0] * (n + 1)

    for u in reversed(order):

        total = 0

        for v in graph[u]:
            if parent[v] == u:
                total += max(dp0[v], dp1[v])

        dp0[u] = total

        best = 0

        for v in graph[u]:
            if parent[v] == u:
                cur = total - max(dp0[v], dp1[v]) + dp0[v] + 1
                best = max(best, cur)

        dp1[u] = best

    original_matching = max(dp0[1], dp1[1])

    # Check every removable vertex
    ans = 0

    for remove in range(1, n + 1):

        visited = [False] * (n + 1)

        total_matching = 0

        for start in range(1, n + 1):

            if start == remove or visited[start]:
                continue

            # Build connected component
            comp = []

            q = deque([start])
            visited[start] = True

            while q:
                node = q.popleft()
                comp.append(node)

                for nei in graph[node]:
                    if nei != remove and not visited[nei]:
                        visited[nei] = True
                        q.append(nei)

            # Tree DP on this component
            root = comp[0]

            par = {root: -1}
            ord2 = []

            q = deque([root])

            while q:
                node = q.popleft()
                ord2.append(node)

                for nei in graph[node]:
                    if nei != remove and nei not in par:
                        par[nei] = node
                        q.append(nei)

            d0 = {}
            d1 = {}

            for u in reversed(ord2):

                total = 0

                for v in graph[u]:
                    if v != remove and par.get(v) == u:
                        total += max(d0[v], d1[v])

                d0[u] = total

                best = 0

                for v in graph[u]:
                    if v != remove and par.get(v) == u:
                        cur = total - max(d0[v], d1[v]) + d0[v] + 1
                        best = max(best, cur)

                d1[u] = best

            total_matching += max(d0[root], d1[root])

        if total_matching == original_matching:
            ans += 1

    return ans


def main():
    import sys

    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])

    edges = []

    idx = 1

    for _ in range(n - 1):
        u = int(data[idx])
        v = int(data[idx + 1])

        edges.append((u, v))

        idx += 2

    print(count_removable_vertices(n, edges))


if __name__ == "__main__":
    main()