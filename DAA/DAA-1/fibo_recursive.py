def fibo_recursive(n):

    if n <= 1:
        return n
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)
        
n = int(input("Enter the number of terms: "))
for i in range(n):
    print(fibo_recursive(i), end=" ")

"""
Time Complexity: O(2^n)
--------------------------------
Each call generates two more calls (except at base case),
forming an exponential growth tree of size roughly 2^n.
Example: fib(5) calls fib(4) and fib(3), and both again expand further.

Space Complexity: O(n)
--------------------------------
The maximum depth of the recursion tree is 'n',
so the call stack will hold at most 'n' function calls at once.
"""