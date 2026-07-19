def calculate_max_moons(n, m, moons):
    max_total = 0

    for i in range(n):
        total = sum(moons[i])
        if total > max_total:
            max_total = total

    return max_total


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    m = int(data[1])

    index = 2
    moons = []
    for _ in range(n):
        moons.append(list(map(int, data[index:index + m])))
        index += m

    result = calculate_max_moons(n, m, moons)
    print(result)


if __name__ == "__main__":
    main()