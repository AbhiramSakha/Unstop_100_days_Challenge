def compute_blend_score(N, A):
    result = 0
    for i in range(N):
        freq = (i + 1) * (N - i)
        if freq % 2 == 1:
            result ^= A[i]
    return result

# Input
N = int(input())
A = list(map(int, input().split()))

# Output
print(compute_blend_score(N, A))