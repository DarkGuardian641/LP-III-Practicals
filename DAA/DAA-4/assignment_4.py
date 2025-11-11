# 0-1 Knapsack Problem using Dynamic Programming (with selected items)

def knapsack(weights, values, capacity):
    n = len(values)
    
    # Step 1: Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Step 2: Fill DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(values[i-1] + dp[i-1][w - weights[i-1]], dp[i-1][w])
            else:
                dp[i][w] = dp[i-1][w]

    # Step 3: Backtrack to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i)  # item i was included
            w -= weights[i-1]

    selected_items.reverse()  # To show items in original order

    # Step 4: Return results
    return dp[n][capacity], selected_items


# Example usage
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_value, items = knapsack(weights, values, capacity)
print("Maximum value in Knapsack =", max_value)
print("Items included (1-indexed) =", items)