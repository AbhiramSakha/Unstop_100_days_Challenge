def user_logic(n, arr):
    result = [1] * n

    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= arr[i]

    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= arr[i]

    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    arr = list(map(int, data[1:]))

    result = user_logic(n, arr)

    for res in result:
        print(res)

if __name__ == "__main__":
    main()