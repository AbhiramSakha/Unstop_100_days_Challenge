import sys
import heapq

def dijkstra(start, graph, n):
    INF = 10**20
    dist = [INF] * (n + 1)
    dist[start] = 0
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d != dist[u]:
            continue
        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                heapq.heappush(pq, (nd, v))
    return dist

def main():
    input = sys.stdin.readline

    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    rev = [[] for _ in range(n + 1)]
    edges = []

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        rev[b].append((a, c))
        edges.append((a, b, c))

    dist1 = dijkstra(1, graph, n)
    dist2 = dijkstra(n, rev, n)

    INF = 10**20
    ans = INF

    for a, b, c in edges:
        if dist1[a] == INF or dist2[b] == INF:
            continue
        ans = min(ans, dist1[a] + c // 2 + dist2[b])

    print(ans)

if __name__ == "__main__":
    main()