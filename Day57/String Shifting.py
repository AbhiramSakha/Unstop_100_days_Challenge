def apply_shifts(n, s, shifts):
    res = []

    for i in range(n):
        shift = shifts[i] % 26
        new_char = chr((ord(s[i]) - ord('a') + shift) % 26 + ord('a'))
        res.append(new_char)

    return ''.join(res)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    s = data[1]
    shifts = list(map(int, data[2:2+n]))
    
    result = apply_shifts(n, s, shifts)
    print(result)

if __name__ == "__main__":
    main()