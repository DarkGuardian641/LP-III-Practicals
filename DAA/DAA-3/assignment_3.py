class Item:
    def __init__(self, value, weight):   # ✅ Correct constructor
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # value-to-weight ratio


def fractional_knapsack(capacity, values, weights):
    # Step 1: Create list of items
    items = [Item(values[i], weights[i]) for i in range(len(values))]
    
    # Step 2: Sort items by value/weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)
    
    total_value = 0.0  # Final profit
    
    # Step 3: Take items until knapsack is full
    for item in items:
        if capacity >= item.weight:
            # Take full item
            capacity -= item.weight
            total_value += item.value
        else:
            # Take fraction of item
            total_value += item.value * (capacity / item.weight)
            break  # Knapsack is full
    
    return total_value


# Driver code
if __name__ == "__main__":   # ✅ Correct main check
    values = [60, 100, 120]   # Profits
    weights = [10, 20, 30]    # Weights
    capacity = 50             # Knapsack 
    
    max_value = fractional_knapsack(capacity, values, weights)
    print("Maximum value in Knapsack =", max_value)  # ✅ Fixed print