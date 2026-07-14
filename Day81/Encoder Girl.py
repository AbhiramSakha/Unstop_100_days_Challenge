def processWords(n, s, x):
    ans = []
    for word in s:
        ans.append(len(word) - word.count(x))
    ans.sort()
    return ans


def main():
    n = int(input())
    s = input().split()
    x = input().strip()

    print(*processWords(n, s, x))


if __name__ == "__main__":
    main()