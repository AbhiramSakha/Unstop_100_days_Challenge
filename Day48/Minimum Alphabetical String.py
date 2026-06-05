def get_smallest_string(n, k):
    res = ['a'] * n
    k -= n  
    i = n - 1
    while k > 0:
        add = min(25, k)
        res[i] = chr(ord('a') + add)
        k -= add
        i -= 1

    return ''.join(res)

if __name__ == "__main__":
    n, k = map(int, input().split())
    print(get_smallest_string(n, k))