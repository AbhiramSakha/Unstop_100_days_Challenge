def can_break(s1, s2):
    if len(s1) != len(s2):
        return "false"

    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)

    s1_breaks_s2 = all(a >= b for a, b in zip(s1_sorted, s2_sorted))
    s2_breaks_s1 = all(b >= a for a, b in zip(s1_sorted, s2_sorted))

    return "true" if s1_breaks_s2 or s2_breaks_s1 else "false"

# Input
s1 = input().strip()
s2 = input().strip()

# Output
print(can_break(s1, s2))
                       