def frequency_sort(s):
    freq = {}
    first_index = {}

    for i, ch in enumerate(s):
        freq[ch] = freq.get(ch, 0) + 1
        if ch not in first_index:
            first_index[ch] = i

    chars = sorted(freq.keys(), key=lambda x: (-freq[x], first_index[x]))

    result = []
    for ch in chars:
        result.append(ch * freq[ch])

    return ''.join(result)

def main():
    import sys
    input = sys.stdin.read

    s = input().strip()

    result = frequency_sort(s)
    print(result)

if __name__ == "__main__":
    main()