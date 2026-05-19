def raju_returns_to_origin(n, moves):
    x = 0
    y = 0

    for move in moves:
        if move == 'U':
            y += 1
        elif move == 'D':
            y -= 1
        elif move == 'R':
            x += 1
        elif move == 'L':
            x -= 1

    if x == 0 and y == 0:
        return "YES"
    else:
        return "NO"

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])        # Length of moves string
    moves = data[1]         # The moves string
    
    result = raju_returns_to_origin(n, moves)
    print(result)

if __name__ == "__main__":
    main()