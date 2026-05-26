def compareBits(a, b):
    m = len(a)
    n = len(b)
    total_diff = 0

    for i in range(n - m + 1):  # Loop through each possible substring
        for j in range(m):
            if a[j] != b[i + j]:
                total_diff += 1

    return total_diff

if __name__ == '__main__':
    a = input().strip()
    b = input().strip()
    print(compareBits(a, b))