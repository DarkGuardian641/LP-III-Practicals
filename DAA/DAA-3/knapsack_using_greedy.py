''' 
Write a program to solve a fractional Knapsack problem using a greedy method.
'''

# Function to calculate maximum value in Knapsack
def fractional_knapsack(weight, profit, capacity):
    n = len(profit)
    # Calculate value/weight ratio
    ratio = []
    for i in range(n):
        r = profit[i]/ weight[i]
        ratio.append((r, weight[i], profit[i]))

    # Sort items based on ratio in descending order
    ratio.sort(reverse=True)

    total_profit = 0.0
    total_weight = 0.0

    print("\n Items Considered")
    print("\n Profit, Weight, Ratio")
    for r, w, p in ratio:
        print(f"({p}, {w}, {r:.2f})")

    for r, w, p in ratio:
        if capacity >= w:
            # Take the whole item/obj
            capacity -= w
            total_profit += p
            total_weight += w
            print(f"Took {100}% of object (Profit = {p}, Weight= {w})")
        else:
            # Take fraction of item
            fraction = capacity/w
            total_profit += p*fraction
            total_weight += w*fraction
            print(f"Took {fraction*100}:.2f% of object (Profit = {p}, weight= {w})")
            break  # Knapsack is full

    print("\nTotal Weight in Knapsack:", round(total_weight, 2))
    print("Maximum Profit in Knapsack:", round(total_profit, 2))


# ---- Main Program ----
if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    profit = []
    weight = []
    for i in range(n):
        p = float(input(f"Enter profit of item {i+1}: "))
        w = float(input(f"Enter weight of item {i+1}: "))
        profit.append(p)
        weight.append(w)
    
    capacity = float(input("\nEnter capacity of knapsack: "))
    fractional_knapsack(weight, profit, capacity)