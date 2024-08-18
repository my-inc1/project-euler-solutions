"""
a^2+b^2=c^2

a+b+c=1000

thats it
"""

"""
---Euclid's formula--- learned his name today
a = m^2 - n^2 = (m+n)(m-n)
c = m^2 + n^2 = idk
b = 2mn
"""

"""
a+b+c becomes 2m(m+n) = 1000
im too lazy to prove it
its hard to do math on keyboard sorry
so m(m+n) = 500
"""

"""
the factors are:
"""

factors = [i for i in range(1, 500 + 1) if 500 % i == 0]

for m in factors:
    n = 500 // m - m  # python sucks "//" integer division?
    a = m**2 - n**2
    b = 2 * m * n
    c = m**2 + n**2
    if a > 0 and b > 0 and a**2 + b**2 == c**2:
        print(a, b, c)
        print(a * b * c)

#>31875000
