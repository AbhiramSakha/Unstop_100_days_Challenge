# Enter your code here. Read input from STDIN. Print output to STDOUT
def compute_max_difference(q, queries):
    freq_map = {}  # Stores {number: frequency}

    for a, b in queries:
        freq_map[b] = freq_map.get(b, 0) + a

    if len(freq_map) <= 1:
        print(0)
        return

    # Find min and max frequencies
    freq_values = list(freq_map.values())
    min_freq = min(freq_values)
    max_freq = max(freq_values)

    # Find smallest number with min_freq
    min_freq_nums = [num for num in freq_map if freq_map[num] == min_freq]
    smallest_num = min(min_freq_nums)

    # Find largest number with max_freq
    max_freq_nums = [num for num in freq_map if freq_map[num] == max_freq]
    largest_num = max(max_freq_nums)

    print(abs(largest_num - smallest_num))

if __name__ == "__main__":
    q = int(input())
    queries = [tuple(map(int, input().split())) for _ in range(q)]
    compute_max_difference(q, queries)
                            