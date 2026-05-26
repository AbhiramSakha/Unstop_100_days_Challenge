from collections import deque

def can_score_exact_runs(arr):
    n = len(arr)
    target = n - 1
    if n == 0:
        return False
    if target == 0:
        return True  # Already at index 0 = target 0 with zero jumps
    
    visited = [False] * n
    visited[0] = True
    queue = deque([0])
    
    # Track the furthest not yet expanded
    max_reached = 0
    
    while queue:
        i = queue.popleft()
        reach = min(n - 1, i + arr[i])
        start = max(max_reached + 1, i + 1)
        
        for nxt in range(start, reach + 1):
            if not visited[nxt]:
                visited[nxt] = True
                if nxt == target:
                    return True
                queue.append(nxt)
        
        max_reached = max(max_reached, reach)
    
    return False

def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    print(str(can_score_exact_runs(arr)).lower())

if __name__ == "__main__":
    main()