import heapq

def user_logic(N, M, edges):
    graph = [[] for _ in range(N + 1)]
    for idx, (u, v, w) in enumerate(edges):
        graph[u].append((v, w, idx))
        graph[v].append((u, w, idx))

    used = [False] * M
    INF = 10 ** 18

    for s in range(1, N + 1):
        dist = [INF] * (N + 1)
        dist[s] = 0
        pq = [(0, s)]

        while pq:
            d, u = heapq.heappop(pq)
            if d != dist[u]:
                continue
            for v, w, _ in graph[u]:
                nd = d + w
                if nd < dist[v]:
                    dist[v] = nd
                    heapq.heappush(pq, (nd, v))

        for idx, (u, v, w) in enumerate(edges):
            if dist[u] + w == dist[v] or dist[v] + w == dist[u]:
                used[idx] = True

    return M - sum(used)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    N = int(data[0])
    M = int(data[1])
    edges = []
    index = 2
    for _ in range(M):
        u = int(data[index])
        v = int(data[index + 1])
        c = int(data[index + 2])
        edges.append((u, v, c))
        index += 3

    result = user_logic(N, M, edges)
    print(result)

if __name__ == "__main__":
    main()