n = int(input())

items = []
for _ in range(n):
    items.append(input().split())

ruleKey = input().strip()
ruleValue = input().strip()

key_index = {"type": 0, "color": 1, "name": 2}

index = key_index[ruleKey]

count = 0
for item in items:
    if item[index] == ruleValue:
        count += 1


print(count)