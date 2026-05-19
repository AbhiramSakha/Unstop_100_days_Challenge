def longest_palindromic_substring_length(s):
    # Transform the string (add separators to handle even-length palindromes)
    t = '#' + '#'.join(s) + '#'
    n = len(t)
    p = [0] * n
    c = r = 0  # center and right boundary

    for i in range(n):
        mirror = 2*c - i
        if i < r:
            p[i] = min(r - i, p[mirror])
        # Expand around center
        a = i + p[i] + 1
        b = i - p[i] - 1
        while a < n and b >= 0 and t[a] == t[b]:
            p[i] += 1
            a += 1
            b -= 1
        # Update center and right boundary
        if i + p[i] > r:
            c = i
            r = i + p[i]

    return max(p)

# Input
n = int(input())
s = input().strip()

# Output
print(longest_palindromic_substring_length(s))
                         