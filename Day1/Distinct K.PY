# Enter your code here. Read input from STDIN. Print output to STDOUT
def find_kth_unique_string(n, strings, k):
    from collections import Counter
    freq = Counter(strings)

    unique_strings = []
    for s in strings:
        if freq[s] == 1:
            unique_strings.append(s)

    if len(unique_strings) >= k:
        return unique_strings[k - 1]
    else:
        return "-1"

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    n = int(data[0])
    strings = data[1:n+1]
    k = int(data[n+1])

    result = find_kth_unique_string(n, strings, k)
    print(result)

if __name__ == "__main__":
    main()
                         