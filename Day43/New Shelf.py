def calculate_inverse_of_lis_length(n, heights):
    MOD = 1000007

    lis = []

    for x in heights:
        left, right = 0, len(lis)
        while left < right:
            mid = (left + right) // 2
            if lis[mid] < x:
                left = mid + 1
            else:
                right = mid
        if left == len(lis):
            lis.append(x)
        else:
            lis[left] = x

    length = len(lis)

    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        g, x1, y1 = extended_gcd(b, a % b)
        return g, y1, x1 - (a // b) * y1

    g, x, _ = extended_gcd(length, MOD)
    return (x % MOD + MOD) % MOD


if __name__ == '__main__':
    n = int(input())
    heights = list(map(int, input().split()))
    result = calculate_inverse_of_lis_length(n, heights)
    print(result)