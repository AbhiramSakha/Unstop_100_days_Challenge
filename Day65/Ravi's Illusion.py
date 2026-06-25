def illusion_of_array(n, arr):
    MOD = 10**9 + 7

    left = [0] * n
    right = [0] * n

    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()

        left[i] = i + 1 if not stack else i - stack[-1]
        stack.append(i)

    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()

        right[i] = n - i if not stack else stack[-1] - i
        stack.append(i)

    ans = 0
    for i in range(n):
        ans = (ans + arr[i] * left[i] * right[i]) % MOD

    return ans

def main():
    import sys
    data = sys.stdin.read().strip().split()

    n = int(data[0])
    arr = list(map(int, data[1:]))

    print(illusion_of_array(n, arr))

if __name__ == "__main__":
    main()