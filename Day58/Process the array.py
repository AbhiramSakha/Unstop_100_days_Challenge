def user_logic(n, arr):
    res = []
    i, j = 0, n - 1

    while i <= j:
        res.append(arr[j])
        j -= 1

        if i <= j:
            res.append(arr[i])
            i += 1

    s = n // 2
    return res[s:] + res[:s]

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    arr = list(map(int, data[1:]))

    result = user_logic(n, arr)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()