from collections import defaultdict, deque

def solve():
    k = int(input())
    n = int(input())
    m = int(input())
    edge_count = int(input())
    
    graph = defaultdict(list)

    for _ in range(edge_count):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    visited = set()
    q = deque([0])
    visited.add(0)
    
    count = 0

    while q:
        curr = q.popleft()

        # Check non-functional only if M != 0
        if m != 0 and curr != 0 and curr % m == 0:
            count += 1

        for neighbor in graph[curr]:
            if neighbor not in visited:
                visited.add(neighbor)
                q.append(neighbor)
    
    print(count * k)

solve()
                       