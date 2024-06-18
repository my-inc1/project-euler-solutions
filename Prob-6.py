#Find the difference between the sum of the squares of the first
#one hundred natural numbers and the square of the sum.

## I used Guass method to loop through the numbers
def summaTion(a, b, f):
    total = 0
    for i in range(a, b + 1):
        total += f(i)
    return total

# squaresumOf as the sum of squares
def sumOfSquares(i):
    return i * i

res_sumOfSquares = summaTion(1, 100, sumOfSquares)

# summation of integers from 1 to 100
def identity(i):
    return i

sum_of_integers = summaTion(1, 100, identity)
squaresumOf = sum_of_integers ** 2

print(squaresumOf - res_sumOfSquares)
