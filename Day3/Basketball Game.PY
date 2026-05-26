def user_logic(ops):
    record = []

    for op in ops:
        if op == "+":
            if len(record) >= 2:
                record.append(record[-1] + record[-2])
        elif op == "D":
            if record:
                record.append(2 * record[-1])
        elif op == "C":
            if record:
                record.pop()
        else:
            # Convert to int safely
            try:
                record.append(int(op))
            except ValueError:
                continue  # ignore invalid input strings just in case

    return sum(record)

if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read().split()
    n = int(input_data[0])
    ops = input_data[1:]

    result = user_logic(ops)
    print(result)