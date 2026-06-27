from collections import Counter

def user_logic(str1, str2, k):
    def longest_palindrome(s):
        n = len(s)
        start = 0
        max_len = 1

        for i in range(n):
            # Odd length
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1 > max_len) or (
                    r - l + 1 == max_len and l > start
                ):
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1

            # Even length
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if (r - l + 1 > max_len) or (
                    r - l + 1 == max_len and l > start
                ):
                    start = l
                    max_len = r - l + 1
                l -= 1
                r += 1

        return s[start:start + max_len]

    s1 = longest_palindrome(str1)
    s2 = longest_palindrome(str2)

    need = Counter(s2)
    have = Counter()

    required = len(need)
    formed = 0
    left = 0
    ans = float("inf")

    for right in range(len(s1)):
        ch = s1[right]

        if ch in need:
            have[ch] += 1
            if have[ch] == need[ch]:
                formed += 1

        while formed == required:
            ans = min(ans, right - left + 1)

            ch = s1[left]
            if ch in need:
                if have[ch] == need[ch]:
                    formed -= 1
                have[ch] -= 1
            left += 1

    if ans == float("inf"):
        return "NO"

    return "YES" if ans >= k else "NO"


def main():
    import sys

    data = sys.stdin.read().split()

    str1 = data[0]
    str2 = data[1]
    k = int(data[2])

    print(user_logic(str1, str2, k))


if __name__ == "__main__":
    main()