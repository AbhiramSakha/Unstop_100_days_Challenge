def user_logic(n, x, s):
    visited = {x}
    pos = x

    for ch in s:
        if ch == 'L':
            pos -= 1
        else:
            pos += 1
        visited.add(pos)

    return len(visited)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for _ in range(T):
        n = int(data[idx])
        x = int(data[idx + 1])
        s = data[idx + 2]
        idx += 3
        
        # Call user logic function and store the result
        result = user_logic(n, x, s)
        results.append(result)
    
    # Print all results for each test case
    for result in results:
        print(result)

if __name__ == "__main__":
    main()