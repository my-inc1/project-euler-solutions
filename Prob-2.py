def even_fib_sum(limit):
    a, b = 0, 2  # Start with the first two even Fibonacci numbers (0 and 2)
    while a <= limit:
        yield a
        a, b = b, 4 * b + a  # Generate the next even Fibonacci number directly

# Calculate the sum of even Fibonacci numbers up to the limit
print(sum(even_fib_sum(4000000)))

## answer:
4613732
