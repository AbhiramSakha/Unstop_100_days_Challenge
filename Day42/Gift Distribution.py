def user_logic(n):
    total = n * (n + 1) // 2

    if total % 2:
        return (False,)

    target = total // 2
    set1 = []
    set2 = []

    for i in range(n, 0, -1):
        if i <= target:
            set1.append(i)
            target -= i
        else:
            set2.append(i)

    return (True, set1, set2)


def main():
    import sys
    input = sys.stdin.read
    data = input().strip()

    n = int(data)

    result = user_logic(n)

    if result[0]:
        print("YES")
        set1 = result[1]
        set2 = result[2]

        print(len(set1))
        print(*set1)

        print(len(set2))
        print(*set2)
    else:
        print("NO")


if __name__ == "__main__":
    main()