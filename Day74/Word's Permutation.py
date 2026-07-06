from math import factorial
from collections import Counter

def user_logic(s):
    """
    Write your logic here.
    Parameters:
        s (str): The input word
    Returns:
        int: The number of distinct permutations where the letter with the highest frequency does not appear together
    """
    freq = Counter(s)

    # Choose any character with maximum frequency
    ch = max(freq, key=freq.get)
    mx = freq[ch]

    # Total distinct permutations
    total = factorial(len(s))
    for c in freq.values():
        total //= factorial(c)

    # Permutations where all occurrences of the chosen character are together
    block_freq = freq.copy()
    block_freq.pop(ch)
    block_len = len(s) - mx + 1

    together = factorial(block_len)
    for c in block_freq.values():
        together //= factorial(c)

    return total - together


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    T = int(data[0])
    ans = []

    for i in range(1, T + 1):
        ans.append(user_logic(data[i]))

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()