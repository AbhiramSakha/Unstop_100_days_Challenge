def numTrees(n):
    # Dynamic Programming approach to compute Catalan numbers
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: There's one empty tree
    
    for nodes in range(1, n + 1):
        for root in range(1, nodes + 1):
            left = root - 1          # Nodes in left subtree
            right = nodes - root     # Nodes in right subtree
            dp[nodes] += dp[left] * dp[right]
    
    return dp[n]

if __name__ == '__main__':
    number_of_nodes = int(input())
    print(numTrees(number_of_nodes))