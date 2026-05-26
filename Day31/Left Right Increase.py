def user_logic(n, p, array):
    current = array[:]

    for _ in range(p):
        add = [0] * n

        for i in range(n):
            if current[i] != 0:
                if i > 0:
                    add[i - 1] += 2
                if i < n - 1:
                    add[i + 1] += 2

        for i in range(n):
            current[i] += add[i]

    return sum(current) - sum(array)


def main():
    import sys

    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    p = int(data[1])

    array = list(map(int, data[2:2 + n]))

    result = user_logic(n, p, array)

    print(result)


if __name__ == "__main__":
    main()