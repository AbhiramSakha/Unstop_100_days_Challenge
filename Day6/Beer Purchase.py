def max_bottle_cost(n, x, costs):
    costs.sort()
    total_bottles = 0
    day = 0

    while True:
        count = 0
        current_sum = 0
        for i in range(n):
            price_today = costs[i] + day
            if price_today > x:
                break
            if current_sum + price_today <= x:
                current_sum += price_today
                count += 1
            else:
                break

        if count == 0:
            break

        # Max number of consecutive extra days you can afford this exact selection
        extra_days = (x - current_sum) // count
        total_bottles += count * (extra_days + 1)
        day += (extra_days + 1)

    return total_bottles


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])  # number of shops
    x = int(data[1])  # daily budget
    costs = list(map(int, data[2:]))

    result = max_bottle_cost(n, x, costs)
    print(result)


if __name__ == "__main__":
    main()