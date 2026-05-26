def process_queries(q, queries):
    stock = {}
    for query in queries:
        if query[0] == '1':
            # Add chocolates
            choco_type = query[1]
            qty = int(query[2])
            stock[choco_type] = stock.get(choco_type, 0) + qty
        elif query[0] == '2':
            # Sell chocolates
            choco_type = query[1]
            qty = int(query[2])
            available = stock.get(choco_type, 0)
            to_sell = min(qty, available)
            print(to_sell)
            stock[choco_type] = available - to_sell

if __name__ == "__main__":
    q = int(input())
    queries = [input().split() for _ in range(q)]
    process_queries(q, queries)
                            