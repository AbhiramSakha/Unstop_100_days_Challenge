def user_logic(n, enemy_groups, m):
    def can_finish(k):
        minutes = 0
        for enemies in enemy_groups:
            minutes += (enemies + k - 1) // k
        return minutes <= m

    left, right = 1, max(enemy_groups)
    ans = right

    while left <= right:
        mid = (left + right) // 2
        if can_finish(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans, oct(ans)[2:]

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    enemy_groups = list(map(int, data[1:n + 1]))
    m = int(data[n + 1])

    result = user_logic(n, enemy_groups, m)

    if result:
        k, octal_k = result
        print(f"{k} {octal_k}")
    else:
        print(1)

if __name__ == "__main__":
    main()