MOD = 10**9 + 7

def count_paths(n, m, roads):
    from collections import deque

    graph = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)

    for u, v in roads:
        graph[u].append(v)
        indegree[v] += 1

    # Topological Sort (Kahn's Algorithm)
    q = deque()
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    dp = [0] * (n + 1)
    dp[1] = 1

    while q:
        u = q.popleft()
        for v in graph[u]:
            dp[v] = (dp[v] + dp[u]) % MOD
            indegree[v] -= 1
            if indegree[v] == 0:
                q.append(v)

    return dp[n]

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # Number of landmarks
    m = int(data[1])  # Number of one-way roads
    
    roads = []
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        roads.append((u, v))
        index += 2

    # Call user logic function and print the output
    result = count_paths(n, m, roads)
    print(result)

if __name__ == "__main__":
    main()