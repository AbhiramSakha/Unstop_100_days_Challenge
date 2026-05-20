class MyHashMap:
    def __init__(self, size=10007):
        self.size = size  # prime number for hashing
        self.buckets = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def insert(self, key, value):
        h = self._hash(key)
        bucket = self.buckets[h]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))

    def get(self, key):
        h = self._hash(key)
        bucket = self.buckets[h]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def delete(self, key):
        h = self._hash(key)
        bucket = self.buckets[h]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return


def process_queries(queries):
    results = []
    hashmap = MyHashMap()
    for query in queries:
        if query[0] == 1:
            _, key, value = query
            hashmap.insert(key, value)
        elif query[0] == 2:
            _, key = query
            results.append(hashmap.get(key))
        elif query[0] == 3:
            _, key = query
            hashmap.delete(key)
    return results


# ------------------- Main -------------------
import sys
input = sys.stdin.read
data = input().strip().split()

# Read number of queries
n = int(data[0])
index = 1

queries = []

for _ in range(n):
    query_type = int(data[index])
    if query_type == 1:
        key = int(data[index + 1])
        value = int(data[index + 2])
        queries.append((1, key, value))
        index += 3
    elif query_type == 2:
        key = int(data[index + 1])
        queries.append((2, key))
        index += 2
    elif query_type == 3:
        key = int(data[index + 1])
        queries.append((3, key))
        index += 2

# Process the queries
results = process_queries(queries)

# Print output for type 2 queries
for result in results:
    print(result)