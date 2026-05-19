def count_consistent_cars(components, models):
    allowed_set = set(components)
    count = 0

    for model in models:
        if all(char in allowed_set for char in model):
            count += 1
    return count

if __name__ == "__main__":
    import sys
    data = sys.stdin.read().split()
    
    components = data[0]
    n = int(data[1])  # Not needed for logic but matches input format
    models = data[2:]  # Remaining items are the models

    result = count_consistent_cars(components, models)
    print(result)