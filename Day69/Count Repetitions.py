def number_of_days_when_subsequence(S, T):
    from bisect import bisect_right

    pos = {}
    for i, ch in enumerate(S):
        if ch not in pos:
            pos[ch] = []
        pos[ch].append(i)

    n = len(S)
    days = 1
    cur = -1

    for ch in T:
        if ch not in pos:
            return -1

        lst = pos[ch]
        idx = bisect_right(lst, cur)

        if idx == len(lst):
            days += 1
            cur = lst[0]
        else:
            cur = lst[idx]

    return days


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    S = data[0]
    T = data[1]

    result = number_of_days_when_subsequence(S, T)
    print(result)


if __name__ == "__main__":
    main()