def count_optimal_positions(coords):
    x_coords = sorted([x for x, y in coords])
    y_coords = sorted([y for x, y in coords])
    n = len(coords)

    # Handle even and odd separately
    if n % 2 == 1:
        # Odd number of lakes → only one median
        return 1
    else:
        # Even number of lakes → range of medians
        x1 = x_coords[n // 2 - 1]
        x2 = x_coords[n // 2]
        y1 = y_coords[n // 2 - 1]
        y2 = y_coords[n // 2]
        return (x2 - x1 + 1) * (y2 - y1 + 1)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    coords = []
    for i in range(n):
        x = int(data[1 + 2 * i])
        y = int(data[2 + 2 * i])
        coords.append((x, y))

    result = count_optimal_positions(coords)
    print(result)

if __name__ == "__main__":
    main()