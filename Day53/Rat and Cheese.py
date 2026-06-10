from collections import deque
import sys
input = sys.stdin.read

def minimumTime(grid):
    n = len(grid)
    q = deque()
    cheese = 0

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 2:
                q.append((i, j, 0))
            elif grid[i][j] == 1:
                cheese += 1

    if cheese == 0:
        return 0

    visited = [[False] * n for _ in range(n)]
    for i, j, _ in q:
        visited[i][j] = True

    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    eaten = 0
    max_time = 0

    while q:
        x, y, t = q.popleft()

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if grid[nx][ny] == 1:
                    visited[nx][ny] = True
                    eaten += 1
                    max_time = max(max_time, t + 1)
                    q.append((nx, ny, t + 1))

    return max_time if eaten == cheese else -1

if __name__ == '__main__':
    data = input().split()
    n = int(data[0])

    grid = []
    idx = 1
    for _ in range(n):
        row = list(map(int, data[idx:idx + n]))
        grid.append(row)
        idx += n

    print(minimumTime(grid))