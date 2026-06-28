from collections import Counter

def shortest_substring_length(S, L):
    need = Counter(L)
    window = {}
    required = len(need)
    formed = 0

    left = 0
    ans = float('inf')

    for right in range(len(S)):
        c = S[right]
        window[c] = window.get(c, 0) + 1

        if c in need and window[c] == need[c]:
            formed += 1

        while formed == required:
            ans = min(ans, right - left + 1)

            ch = S[left]
            window[ch] -= 1

            if ch in need and window[ch] < need[ch]:
                formed -= 1

            left += 1

    return -1 if ans == float('inf') else ans


def main():
    import sys
    data = sys.stdin.read().splitlines()

    S = data[0].rstrip()
    L = data[1].rstrip()

    print(shortest_substring_length(S, L))

if __name__ == "__main__":
    main()