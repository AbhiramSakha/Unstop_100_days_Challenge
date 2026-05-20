def min_time_to_print(s):
    s = ''.join(sorted(s))
    current = 'a'
    total_time = 0

    for char in s:
        diff = abs(ord(char) - ord(current))
        move_time = min(diff, 26 - diff) 
        total_time += move_time + 1  
        current = char

    return total_time

s = input().strip()
print(min_time_to_print(s))