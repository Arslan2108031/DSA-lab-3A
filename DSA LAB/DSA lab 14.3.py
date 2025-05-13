def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]],
                               dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5
print("Maximum value in Knapsack:", knapsack(weights, values, capacity)) 
print("\nTime Complexity:")
print("- O(n * W) where n = number of items and W = capacity of knapsack")
print("\nReal-World Applications:")
print("- Budget optimization (max value within cost limit)")
print("- Cargo loading (max profit within weight limit)")
print("- Resource allocation (max utility within resource constraint)")
