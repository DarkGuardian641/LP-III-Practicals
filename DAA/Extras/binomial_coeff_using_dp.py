# Program to generate Binomial Coefficients using Dynamic Programming

def binomial_coefficient(n, k):
    # Create a 2D DP table to store values of C(n, k)
    C = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    # Calculate value of Binomial Coefficient in bottom-up manner
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Base Cases
            if j == 0 or j == i:
                C[i][j] = 1
            else:
                # Using Pascal’s Rule: C(n,k) = C(n-1,k-1) + C(n-1,k)
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j]

    return C[n][k]


# Driver code
n = int(input("Enter value of n: "))
k = int(input("Enter value of k: "))

print(f"Binomial Coefficient C({n}, {k}) = {binomial_coefficient(n, k)}")