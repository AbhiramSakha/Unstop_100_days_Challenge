import sys
input = sys.stdin.read

def maximumUnits(boxTypes, truckSize):
    # Sort by units per box in descending order
    boxTypes.sort(key=lambda x: x[1], reverse=True)

    total_units = 0

    for boxes, units in boxTypes:
        take = min(boxes, truckSize)
        total_units += take * units
        truckSize -= take
        if truckSize == 0:
            break

    return total_units

if __name__ == "__main__":
    data = input().split()

    n = int(data[0])
    m = int(data[1])

    boxTypes = []
    idx = 2
    for _ in range(n):
        boxTypes.append([int(data[idx]), int(data[idx + 1])])
        idx += m

    truckSize = int(data[idx])

    print maximumUnits(boxTypes, truckSize)