## Fibonacci numbers

def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

# Example usage:
print(fibonacci(100))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]