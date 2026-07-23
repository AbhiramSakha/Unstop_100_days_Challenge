from collections import Counter

def user_logic(n, x, arr):
    freq = Counter(arr)
    ans = sum(num for num, cnt in freq.items() if cnt == x)
    return ans if ans != 0 or any(cnt == x for cnt in freq.values()) else -1

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    index = 0
    T = int(data[index])
    index += 1
    results = []

    for _ in range(T):
        N = int(data[index])
        X = int(data[index + 1])
        index += 2
        arr = list(map(int, data[index:index + N]))
        index += N

        results.append(user_logic(N, X, arr))

    print(*results, sep="\n")

if __name__ == "__main__":
    main()