def queens_attack_the_king(queens, king):
    qset = {(x, y) for x, y in queens}
    kx, ky = king
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]
    found = []  
    for dx, dy in directions:
        x, y = kx + dx, ky + dy
        while 0 <= x < 8 and 0 <= y < 8:
            if (x, y) in qset:
                found.append((dx, dy, x, y))
                break
            x += dx
            y += dy
    found.sort(key=lambda t: (t[0], t[1]))

    return [[x, y] for _, __, x, y in found]


def main():
    import sys
    data = sys.stdin.read().strip().split()
    n = int(data[0])

    queens = []
    idx = 1
    for _ in range(n):
        x = int(data[idx])
        y = int(data[idx + 1])
        queens.append([x, y])
        idx += 2

    king = [int(data[idx]), int(data[idx + 1])]

    res = queens_attack_the_king(queens, king)

    out = []
    for x, y in res:
        out.append(str(x))
        out.append(str(y))
    print(" ".join(out))


if __name__ == "__main__":
    main()
                