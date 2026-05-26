def user_logic(l, r):
    if l == r:
        return 0

    if l <= (r + 1) // 2:
        return (r - 1) // 2
    else:
        return r - l

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    t = int(data[0])

    results = []
    index = 1

    for _ in range(t):
        l = int(data[index])
        r = int(data[index + 1])
        index += 2

        result = user_logic(l, r)
        results.append(result)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()