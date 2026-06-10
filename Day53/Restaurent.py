def user_logic(n, orders):
    tables = [[] for _ in range(n)]

    for table, item in orders:
        tables[table].append(item)

    for i in range(n):
        tables[i].sort()

    return tables

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()

    n = int(data[0])
    m = int(data[1])

    orders = []
    index = 2
    for _ in range(m):
        table = int(data[index])
        item = data[index + 1]
        orders.append((table, item))
        index += 2

    result = user_logic(n, orders)

    for i in range(n):
        if i < len(result):
            print(" ".join(result[i]))
        else:
            print("")

if __name__ == "__main__":
    main()