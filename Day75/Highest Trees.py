from collections import deque

def user_logic(n, k, heights):
    dq = deque()
    result = []

    for i in range(n):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and heights[dq[-1]] <= heights[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(heights[dq[0]])

    return result


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    k = int(data[1])
    heights = list(map(int, data[2:]))

    result = user_logic(n, k, heights)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()