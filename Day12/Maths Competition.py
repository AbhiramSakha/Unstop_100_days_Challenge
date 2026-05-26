def min_time_to_solve(N, K, A):
    if K == 0:
        return 0
    if N == 0 or not A:
        return -1

    def can_solve_all_in_time(T):
        total = 0
        for time in A:
            if time != 0:
                total += T // time
                if total >= K:
                    return True
        return total >= K

    left, right = 1, max(A) * K
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if can_solve_all_in_time(mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

# Input
N_K = input().split()
N, K = int(N_K[0]), int(N_K[1])
A = list(map(int, input().split())) if N > 0 else []

# Output
print(min_time_to_solve(N, K, A))
                            