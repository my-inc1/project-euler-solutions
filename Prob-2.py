def Fib_in_even(lim):
    a, b = 0, 1
    while a < lim:
        if not a % 2:
            yield a
        a, b = b, a + b

# Create a list from the generator and print the sum of the list
print(sum(Fib_in_even(4000000)))

## answer:
4613732
