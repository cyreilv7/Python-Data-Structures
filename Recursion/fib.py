# return nth fibonacci number

def fib(n):
    if n >= 3:
        return fib(n-1) + fib(n-2)
    return 1

print(fib(20)) # expected: 8