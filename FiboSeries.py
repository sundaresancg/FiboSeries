
def fibonacci(n):
    a = -1
    b = 1
    i = 0
    fibo = []
    while i < n :
        t = a + b
        fibo.append(t)
        a = b
        b = t
        i += 1
    return fibo

print("Fibonacci Series".center(30,'-'))
n = int(input("Enter no. of terms: "))
print(fibonacci(n))
