def user_logic(arr1, arr2):
    x1 = 0
    for x in arr1:
        x1 ^= x

    x2 = 0
    for x in arr2:
        x2 ^= x

    return x1 & x2


def main():
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    print(user_logic(arr1, arr2))


if __name__ == "__main__":
    main()