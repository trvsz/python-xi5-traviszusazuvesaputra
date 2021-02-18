import Fibo

def fib(n): #Write Fibonacci Series Up to n
    a, b = 0, 1
    while a < n:
        print(a, end='')
        a, b = b, a+b
    print()

def fib2(n): #Write Fibonacci Series Up to n
    result = []
    a, b = 0, 1
    while a< n:
        result.append(a)
        a, b = b, a+b
    return result

print(Fibo.fib(100))
print(Fibo.fib(100))

fib = Fibo.fib
print(fib(100))