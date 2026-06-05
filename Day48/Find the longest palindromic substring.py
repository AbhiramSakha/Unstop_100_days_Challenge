import sys

# Placeholder for user logic function
def longestPalindrome(s):
    if len(s) == 0:
        return ""

    start, end = 0, 0

    for i in range(len(s)):
        len1 = expandAroundCenter(s, i, i)       # Odd-length palindromes
        len2 = expandAroundCenter(s, i, i + 1)   # Even-length palindromes
        max_len = max(len1, len2)
        if max_len > end - start:
            start = i - (max_len - 1) // 2
            end = i + max_len // 2

    return s[start:end + 1]

def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

if __name__ == "__main__":
    s = sys.stdin.read().strip()  # Read input string
    result = longestPalindrome(s)
    print(result)