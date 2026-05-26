def good_sum(N, A):
    stack = []
    for i in range(N):
        x = A[i]
        if x >= 0:
            stack.append(x)
        else:
            target = abs(x)
            removed = []
            running_sum = 0

            # Remove minimum number of elements from the end such that sum >= abs(x)
            while stack and running_sum < target:
                val = stack.pop()
                running_sum += val
                removed.append(val)

            if running_sum >= target:
                # If enough sum is collected, just discard those and push abs(x)
                stack.append(target)
            else:
                # If not enough sum collected, discard everything and push abs(x)
                stack = [target]
    
    return sum(stack)

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])  # First input is the integer N
    A = list(map(int, data[1:]))  # Remaining input is the array of integers
    
    # Call user logic function and print the output
    result = good_sum(N, A)
    print(result)

if __name__ == "__main__":
    main()