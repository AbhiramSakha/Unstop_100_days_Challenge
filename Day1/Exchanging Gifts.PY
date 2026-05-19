def find_youngest_member(n, m, gifts):
    from collections import defaultdict

    received_count = defaultdict(int)
    givers = set()

    for a, b in gifts:
        givers.add(a)
        received_count[b] += 1

    for member in range(1, n + 1):
        if received_count[member] == n - 1 and member not in givers:
            return member

    return -1
pass


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    n = int(data[0])  # Number of family members
    m = int(data[1])  # Number of gifts exchanged
    
    gifts = []
    index = 2
    for _ in range(m):
        a_i = int(data[index])
        b_i = int(data[index + 1])
        gifts.append((a_i, b_i))
        index += 2
    
    # Call user logic function and print the output
    result = find_youngest_member(n, m, gifts)
    print(result)

if __name__ == "__main__":
    main()
                          