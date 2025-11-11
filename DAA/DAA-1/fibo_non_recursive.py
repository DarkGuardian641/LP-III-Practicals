def nonrecursive_fibo(n):
    a,b = 0,1
    for i in range(n):
        print(a) 
        a,b = b, a+b

n = int(input("Enter a number: "))
print(nonrecursive_fibo(n))