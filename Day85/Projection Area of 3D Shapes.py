def projection_area(grid):
    n = len(grid)

    top = 0
    front = 0
    side = 0

    for i in range(n):
        row_max = 0
        col_max = 0
        for j in range(n):
            if grid[i][j] > 0:
                top += 1
            row_max = max(row_max, grid[i][j])
            col_max = max(col_max, grid[j][i])

        front += row_max
        side += col_max

    return top + front + side


def main():
    import sys
    data = list(map(int, sys.stdin.read().split()))

    n = data[0]
    grid = []
    idx = 1

    for _ in range(n):
        grid.append(data[idx:idx + n])
        idx += n

    result = projection_area(grid)
    print(result)


if __name__ == "__main__":
    main()