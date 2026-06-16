import heapq

def user_logic(K, N, M, W, D):
    wash_heap = []
    for w in W:
        heapq.heappush(wash_heap, (w, w))

    wash = []
    for _ in range(K):
        t, w = heapq.heappop(wash_heap)
        wash.append(t)
        heapq.heappush(wash_heap, (t + w, w))

    wash.sort()

    def possible(T):
        slots = []

        for d in D:
            cnt = T // d
            if cnt > K:
                cnt = K

            for j in range(1, cnt + 1):
                slots.append(T - j * d)

            if len(slots) > K:
                slots = sorted(slots)[-K:]

        if len(slots) < K:
            return False

        slots.sort()

        if len(slots) > K:
            slots = slots[-K:]

        for w, s in zip(wash, slots):
            if w > s:
                return False

        return True

    lo = 0
    hi = max(wash) + max(D) * K

    while lo < hi:
        mid = (lo + hi) // 2

        if possible(mid):
            hi = mid
        else:
            lo = mid + 1

    return lo


if __name__ == "__main__":
    import sys

    data = list(map(int, sys.stdin.read().split()))

    K, N, M = data[0], data[1], data[2]

    idx = 3
    W = data[idx:idx + N]
    idx += N

    D = data[idx:idx + M]

    print(user_logic(K, N, M, W, D))