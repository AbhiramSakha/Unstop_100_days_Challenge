def min_plants_to_make_palindrome(s):
    # Replace the last character with 'c'
    s = s[:-1] + 'c'
    rev = s[::-1]
    combined = s + "#" + rev
    
    # Compute LPS array (KMP prefix function)
    lps = [0] * len(combined)
    for i in range(1, len(combined)):
        j = lps[i - 1]
        while j > 0 and combined[i] != combined[j]:
            j = lps[j - 1]
        if combined[i] == combined[j]:
            j += 1
        lps[i] = j

    # Minimum characters to add = length of string - longest prefix which is also suffix
    return len(s) - lps[-1]

# Read input
s = input().strip()
print(min_plants_to_make_palindrome(s))