from collections import Counter

def solve(order, s):
    cnt = Counter(s)
    ans = []

    for ch in order:
        if ch in cnt:
            ans.append(ch * cnt[ch])
            del cnt[ch]

    rem = []
    for ch in sorted(cnt.keys()):
        rem.append(ch * cnt[ch])

    return ''.join(ans) + ''.join(rem)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    order = data[0]
    s = data[1]

    result = solve(order, s)
    print(result)

if __name__ == "__main__":
    main()