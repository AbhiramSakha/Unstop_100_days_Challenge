def max_nesting_depth(s):
    max_depth = 0
    current_depth = 0
    
    for char in s:
        if char == '(':
            current_depth += 1
            max_depth = max(max_depth, current_depth)
        elif char == ')':
            current_depth -= 1

    return max_depth

# Input
n = int(input())
s = input().strip()

# Output
print(max_nesting_depth(s))
                            