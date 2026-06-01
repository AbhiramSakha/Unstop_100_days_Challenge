def replace_marks_to_rank(n, marks):
    unique_marks = sorted(set(marks), reverse=True)

    rank_map = {}
    rank = 1
    for mark in unique_marks:
        rank_map[mark] = rank
        rank += 1

    return [rank_map[mark] for mark in marks]

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    n = int(data[0])  # First input is the integer N
    marks = list(map(int, data[1:]))  # Remaining input is the array of marks
    assert len(marks) == n, "The number of marks should match N"
    result = replace_marks_to_rank(n, marks)
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    main()