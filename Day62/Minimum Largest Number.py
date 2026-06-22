def find_largest_number(arr):
    arr.sort()
    a, b = arr[0], arr[1]
    return max(a * 10 + b, b * 10 + a)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = find_largest_number(arr)
    print(result)