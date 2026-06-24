def orderly_queue(s, k):
    if k == 1:
        ans = s
        n = len(s)
        for i in range(1, n):
            ans = min(ans, s[i:] + s[:i])
        return ans

    return ''.join(sorted(s))

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()
    s = data[0]
    k = int(data[1])
    print(orderly_queue(s, k))