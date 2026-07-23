import sys

def findMiddleEarth(a1, a2):
    if len(a1) > len(a2):
        a1, a2 = a2, a1

    m, n = len(a1), len(a2)
    total = m + n
    half = (total + 1) // 2

    left, right = 0, m

    while left <= right:
        i = (left + right) // 2
        j = half - i

        l1 = float('-inf') if i == 0 else a1[i - 1]
        r1 = float('inf') if i == m else a1[i]
        l2 = float('-inf') if j == 0 else a2[j - 1]
        r2 = float('inf') if j == n else a2[j]

        if l1 <= r2 and l2 <= r1:
            if total % 2:
                return float(max(l1, l2))
            return (max(l1, l2) + min(r1, r2)) / 2.0
        elif l1 > r2:
            right = i - 1
        else:
            left = i + 1

    return 0.0


def main():
    input = sys.stdin.read
    data = input().split()
    m = int(data[0])
    n = int(data[1])
    a1 = list(map(int, data[2:m + 2]))
    a2 = list(map(int, data[m + 2:m + n + 2]))
    print(f'{findMiddleEarth(a1, a2):.5f}')


if __name__ == '__main__':
    main()