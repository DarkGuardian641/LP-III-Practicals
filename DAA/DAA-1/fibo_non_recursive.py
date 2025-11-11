def nonrecursive_fibo(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

n = int(input("Enter a number: "))
nonrecursive_fibo(n)


"""
Time Complexity: O(n)
--------------------------------
The loop runs 'n' times, and each iteration performs a constant amount
of work (simple arithmetic and print operation).
Therefore, total time = O(n).

Space Complexity: O(1)
--------------------------------
Only a fixed number of variables (a, b, i) are used regardless of 'n'.
No recursion or additional data structures are used.
Hence, space remains constant.
"""