def knapsack(W, weights, values):
    n = len(weights)
    dp = [[0] * (W + 1) for _ in range(n + 1)]

    for i in range(n):
        for w in range(W + 1):
            if weights[i] > w:
                dp[i+1][w] = dp[i][w]
            else:
                dp[i+1][w] = max(dp[i][w], values[i] + dp[i][w - weights[i]])
    
    return dp[n][W]

print(knapsack(50, [10, 20, 30], [60, 100, 120]))  # Output: 220
