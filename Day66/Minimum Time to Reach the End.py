import heapq

def minimum_time_to_clear_game(matrix):
    n = len(matrix)

    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = matrix[0][0]

    pq = [(matrix[0][0], 0, 0)]
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while pq:
        t, x, y = heapq.heappop(pq)

        if x == n - 1 and y == n - 1:
            return t

        if t > dist[x][y]:
            continue

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                nt = max(t, matrix[nx][ny])

                if nt < dist[nx][ny]:
                    dist[nx][ny] = nt
                    heapq.heappush(pq, (nt, nx, ny))

    return -1


def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))

    n = data[0]
    vals = data[1:]

    matrix = [vals[i * n:(i + 1) * n] for i in range(n)]

    print(minimum_time_to_clear_game(matrix))

if __name__ == "__main__":
    main()