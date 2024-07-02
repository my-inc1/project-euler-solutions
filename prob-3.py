## finding largest prime factor
def largest_prime_factor(n):
    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    largest_factor = None
    # Check for factor of 2 first
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
    
    # Check for odd factors from 3 onwards
    factor = 3
    while factor * factor <= n:
        while (n % factor == 0):
            largest_factor = factor
            n //= factor
        factor += 2

    # If n becomes a prime number greater than 2
    if n > 2 and is_prime(n):
        largest_factor = n
    
    return largest_factor

number = 600851475143
print(largest_prime_factor(number))

## answer:
6857
