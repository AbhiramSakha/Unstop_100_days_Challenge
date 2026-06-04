from collections import Counter

def count_unique_strings(stickers):
    freq = Counter(stickers)

    def dfs():
        total = 0
        for ch in freq:
            if freq[ch] > 0:
                total += 1
                freq[ch] -= 1
                total += dfs()
                freq[ch] += 1
        return total

    return dfs()

def main():
    import sys
    input = sys.stdin.read
    stickers = input().strip()

    result = count_unique_strings(stickers)
    print(result)

if __name__ == "__main__":
    main()