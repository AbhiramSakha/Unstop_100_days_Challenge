import math
def find(m):
    return int(math.isqrt(m))
if __name__ == "__main__":
    m = int(input())
    count = find(m)
    print(count)