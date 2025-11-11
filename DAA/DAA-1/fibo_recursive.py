def fibo_recursive(n):

    if n <= 1:
        return n
    else:
        return fibo_recursive(n-1)+ fibo_recursive(n-2)
        
n = int(input("Enter the number of terms: "))
for i in range(n):
    print(fibo_recursive(i), end=" ")