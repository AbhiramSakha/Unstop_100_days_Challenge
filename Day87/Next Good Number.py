def next_good_number(x):
    x += 1

    while True:
        n = x
        ok = True
        while n:
            if (n % 10) % 2 == 0:
                ok = False
                break
            n //= 10
        if ok:
            return x
        x += 1


def main():
    import sys
    data = sys.stdin.read().split()

    T = int(data[0])
    ans = []

    for i in range(1, T + 1):
        ans.append(str(next_good_number(int(data[i]))))

    sys.stdout.write("\n".join(ans))


if __name__ == "__main__":
    main()