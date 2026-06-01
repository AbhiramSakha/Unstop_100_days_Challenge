def user_logic(arr):
    stack = [float('inf')]
    ans = 0

    for x in arr:
        while stack[-1] <= x:
            mid = stack.pop()
            ans += mid * min(stack[-1], x)
        stack.append(x)

    while len(stack) > 2:
        ans += stack.pop() * stack[-1]

    return ans

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # First input is the integer N
    arr = list(map(int, data[1:]))  # Remaining input is the array of positive integers
    
    # Call user logic function and print the output
    result = user_logic(arr)
    print(result)

if __name__ == "__main__":
    main()