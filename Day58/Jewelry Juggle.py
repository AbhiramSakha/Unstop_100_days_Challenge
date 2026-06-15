def user_logic(a, b, c, d):
    arr = [a, b, c, d]
    total = sum(arr)

    if total % 2:
        return "NO"

    target = total // 2

    for mask in range(1, 16):
        s = 0
        for i in range(4):
            if mask & (1 << i):
                s += arr[i]
        if s == target:
            return "YES"

    return "NO"

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    a = int(data[0])
    b = int(data[1])
    c = int(data[2])
    d = int(data[3])

    result = user_logic(a, b, c, d)
    print(result)

if __name__ == "__main__":
    main()