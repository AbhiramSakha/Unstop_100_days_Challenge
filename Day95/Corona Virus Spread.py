from collections import deque

def infect(grid):
    n = len(grid)
    m = len(grid[0])

    q = deque()
    fresh = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2:
                q.append((i, j, 0))
            elif grid[i][j] == 1:
                fresh += 1

    if fresh == 0:
        return 0
    if not q:
        return -1

    ans = 0
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        x, y, t = q.popleft()
        ans = max(ans, t)

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                grid[nx][ny] = 2
                fresh -= 1
                q.append((nx, ny, t + 1))

    return ans if fresh == 0 else -1


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    m = int(data[1])

    grid = []
    idx = 2
    for _ in range(n):
        grid.append(list(map(int, data[idx:idx + m])))
        idx += m

    print(infect(grid))

if __name__ == "__main__":
    main()