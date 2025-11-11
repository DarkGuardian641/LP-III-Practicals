# Write a program to solve a 0-1 Knapsack problem using dynamic programming 

# 0-1 Knapsack Problem using Dynamic Programming

def knapsack_01(weights, profits, capacity):
    n = len(profits)
    # Create a DP table with (n+1) rows and (capacity+1) columns
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # Include or exclude the item
                dp[i][w] = max(
                    profits[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                # Cannot include the item
                dp[i][w] = dp[i - 1][w]

    # Final answer: maximum profit at dp[n][capacity]
    max_profit = dp[n][capacity]

    # ---- Find which items are included ----
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)
            w -= weights[i - 1]

    selected_items.reverse()

    # Display results
    print("\nDynamic Programming Table:")
    for row in dp:
        print(row)

    print("\nMaximum Profit:", max_profit)
    print("Items included:", selected_items)


# ---- Main Program ----
if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    profits = []
    weights = []

    for i in range(n):
        p = int(input(f"Enter profit of item {i+1}: "))
        w = int(input(f"Enter weight of item {i+1}: "))
        profits.append(p)
        weights.append(w)

    capacity = int(input("\nEnter capacity of knapsack: "))

    knapsack_01(weights, profits, capacity)