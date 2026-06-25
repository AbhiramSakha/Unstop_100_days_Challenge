from collections import Counter
from collections import deque

def longest_subsequence_repeated_k(s, k):
    cnt = Counter(s)

    chars = []
    for c in sorted(cnt.keys(), reverse=True):
        chars.extend([c] * (cnt[c] // k))

    def valid(seq):
        t = seq * k
        j = 0
        for ch in s:
            if j < len(t) and ch == t[j]:
                j += 1
        return j == len(t)

    q = deque([""])
    ans = ""

    while q:
        cur = q.popleft()

        for ch in sorted(set(chars), reverse=True):
            nxt = cur + ch

            if valid(nxt):
                if len(nxt) > len(ans) or (len(nxt) == len(ans) and nxt > ans):
                    ans = nxt
                q.append(nxt)

    return ans

if __name__ == "__main__":
    s = input().strip()
    k = int(input())
    result = longest_subsequence_repeated_k(s, k)
    print(result)