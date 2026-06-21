def snake_to_man_path(matrix, n, m):
    start = end = None

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 's':
                start = (i, j)
            elif matrix[i][j] == 'm':
                end = (i, j)

    if start is None or end is None:
        return 0

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False] * m for _ in range(n)]

    def dfs(x, y):
        if (x, y) == end:
            return 1

        visited[x][y] = True
        paths = 0

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if (0 <= nx < n and 0 <= ny < m and
                not visited[nx][ny] and
                matrix[nx][ny] != 'w'):
                paths += dfs(nx, ny)

        visited[x][y] = False
        return paths

    return dfs(start[0], start[1])


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    m = int(data[1])

    matrix = []
    idx = 2
    for _ in range(n):
        matrix.append(data[idx:idx + m])
        idx += m

    print(snake_to_man_path(matrix, n, m))


if __name__ == "__main__":
    main()