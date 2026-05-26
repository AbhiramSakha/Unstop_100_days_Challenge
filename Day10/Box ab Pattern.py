def is_ab_pattern(s):
    found_b = False
    for char in s:
        if char == 'b':
            found_b = True
        elif char == 'a' and found_b:
            return "NO"
    return "YES"

# Read input
s = input().strip()
print(is_ab_pattern(s))
                            