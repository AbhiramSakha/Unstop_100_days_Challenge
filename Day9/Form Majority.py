# Enter your code here. Read input from STDIN. Print output to STDOUT
def majority_subsequence(votes):
    total_votes = sum(votes)
    half_votes = total_votes / 2
    votes.sort(reverse=True)  # Sort in non-increasing order
    
    majority = []
    current_sum = 0

    for vote in votes:
        current_sum += vote
        majority.append(vote)
        if current_sum > half_votes:
            break
    
    return majority

# Input Reading
n = int(input())
votes = list(map(int, input().split()))

# Compute and print
result = majority_subsequence(votes)
print(*result)
                            