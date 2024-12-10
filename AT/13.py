import time

def knapsack_dp(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(
                    values[i-1] + dp[i-1][w-weights[i-1]],
                    dp[i-1][w]
                )
            else:
                dp[i][w] = dp[i-1][w]

    return dp[n][capacity]




values = [60, 100, 120, 150]
weights = [10, 20, 30, 40]
capacity = 50
n = len(values)

start = time.time()
dp_result = knapsack_dp(values, weights, capacity)
dp_time = time.time() - start

print(f"DP Result: {dp_result}, Time: {dp_time:.6f}s")

