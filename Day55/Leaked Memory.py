def find_crash_details(M1, M2):
    t = 1

    while True:
        if M1 >= M2:
            if M1 < t:
                return (t, M1, M2)
            M1 -= t
        else:
            if M2 < t:
                return (t, M1, M2)
            M2 -= t
        t += 1


def calculate_prefix_sum(arr):
    prefix = []
    s = 0
    for x in arr:
        s += x
        prefix.append(s)
    return prefix


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    M1 = int(data[0])
    M2 = int(data[1])

    crash_time, M1_crash, M2_crash = find_crash_details(M1, M2)

    print(crash_time, M1_crash, M2_crash)

    prefix_sum = calculate_prefix_sum([crash_time, M1_crash, M2_crash])

    print(" ".join(map(str, prefix_sum)))


if __name__ == "__main__":
    main()