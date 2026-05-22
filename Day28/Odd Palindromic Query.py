def process_queries(N, Q, Arr, Query):
    ans = []
    
    for q in Query:
        i = q - 2
        j = q
        expansions = 0
        
        while i >= 0 and j < N and Arr[i] == Arr[j]:
            expansions += 1
            i -= 1
            j += 1
        
        if q == 1:
            ans.append(0)
        else:
            ans.append(2 * expansions + 1)
    
    return ans


def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    
    N = int(data[0])
    Q = int(data[1])
    
    Arr = list(map(int, data[2:N+2]))
    Query = list(map(int, data[N+2:N+2+Q]))
    
    result = process_queries(N, Q, Arr, Query)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
                            