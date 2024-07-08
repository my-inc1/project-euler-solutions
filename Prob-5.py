## Modules needed
import functools
import math

## NOTE: functools is a module for higher order functions (its python, we just import stuff) 

##math.gcd(x, y): Calculates the greatest common divisor (GCD) of x and y.
## x * y // math.gcd(x, y): Computes the least common multiple (LCM) of x and y. 

print(functools.reduce(lambda x,y: x*y//math.gcd(x, y), range(1, 21)))

## output: 232792560
