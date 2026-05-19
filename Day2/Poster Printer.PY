def can_print_sequence(s):
    n = len(s)
    i = 0

    while i < n:
        # Skip white
        if s[i] == 'W':
            i += 1
            continue

        # Start of a non-white segment
        j = i
        has_r = has_b = False

        while j < n and s[j] != 'W':
            if s[j] == 'R':
                has_r = True
            elif s[j] == 'B':
                has_b = True
            j += 1

        # If segment has only R or only B, it's invalid
        if not (has_r and has_b):
            return "NO"

        i = j  # Move to next segment

    return "YES"

# Read input and process all test cases
t = int(input())
for _ in range(t):
    n = int(input())
    s = input().strip()
    print(can_print_sequence(s))