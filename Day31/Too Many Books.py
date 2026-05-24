from bisect import bisect_left

def max_books_on_shelf(heights):
    lis = []

    for h in heights:
        pos = bisect_left(lis, h)

        if pos == len(lis):
            lis.append(h)
        else:
            lis[pos] = h

    return len(lis)

def main():
    import sys

    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])

    heights = list(map(int, data[1:]))

    result = max_books_on_shelf(heights)

    print(result)

if __name__ == "__main__":
    main()