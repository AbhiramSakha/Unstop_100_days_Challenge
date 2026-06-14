def user_logic(n, arr):
    x = arr[0]
    for i in range(1, n):
        x &= arr[i]
    return x

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])
    arr = list(map(int, data[1:]))
    
    result = user_logic(n, arr)
    print(result)

if __name__ == "__main__":
    main()