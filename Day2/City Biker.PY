def highestAltitude(n, arr):
    current_altitude = 0
    max_altitude = 0

    for gain in arr:
        current_altitude += gain
        max_altitude = max(max_altitude, current_altitude)

    return max_altitude

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = highestAltitude(n, arr)
    print(result)