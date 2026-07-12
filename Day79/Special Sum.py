def user_logic(n, nums):
    ans = 0
    prev = None

    for x in nums:
        if x != prev:
            ans += (1 << x)   # 2^x
            prev = x

    return ans


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    nums = list(map(int, data[1:]))

    result = user_logic(n, nums)
    print(result)


if __name__ == "__main__":
    main()