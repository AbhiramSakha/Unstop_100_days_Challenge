def can_reach_home_on_time(n, x, y, z, check_times):
    total_time = sum(check_times) + n * y + z
    return "YES" if total_time <= x else "NO"


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    x = int(data[1])
    y = int(data[2])
    z = int(data[3])
    check_times = list(map(int, data[4:4 + n]))

    result = can_reach_home_on_time(n, x, y, z, check_times)
    print(result)


if __name__ == '__main__':
    main()