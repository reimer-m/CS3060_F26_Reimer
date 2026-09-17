import time
def factorial(n):
    if n < 0:
        raise ValueError("Negative number!")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fact(n):
    if n < 0:
        raise ValueError("Negative number!")

    result = 1
    for i in range(1, n+1):
        result *= i

    return result

n = 6
start = time.perf_counter()
factorial(n)
end = time.perf_counter()
print(f"Recursive took {(end - start) * 1e6:.2f} us")


start = time.perf_counter()
fact(n)
end = time.perf_counter()
print(f"Iterative took {(end - start) * 1e6:.2f} us")

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0,1
    for _ in range(2, n+1):
        a,b = b, a+b
    return b

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

n = 6
start = time.perf_counter()
fibonacci(n)
end = time.perf_counter()
print(f"Iterative took {(end - start) * 1e6:.2f} us")


start = time.perf_counter()
fib(n)
end = time.perf_counter()
print(f"Recursive took {(end - start) * 1e6:.2f} us")