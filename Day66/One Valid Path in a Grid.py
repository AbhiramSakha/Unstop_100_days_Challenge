from collections import deque

dirs = [(0, 1, 1), (0, -1, 2), (1, 0, 3), (-1, 0, 4)]

def minCost(grid):
    n = len(grid)
    m = len(grid[0])

    INF = 10**9
    dist = [[INF] * m for _ in range(n)]
    dist[0][0] = 0

    dq = deque([(0, 0)])

    while dq:
        x, y = dq.popleft()

        for dx, dy, d in dirs:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                cost = dist[x][y] + (0 if grid[x][y] == d else 1)

                if cost < dist[nx][ny]:
                    dist[nx][ny] = cost
                    if grid[x][y] == d:
                        dq.appendleft((nx, ny))
                    else:
                        dq.append((nx, ny))

    return dist[n - 1][m - 1]

def main():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    print(minCost(grid))

if __name__ == "__main__":
    main()