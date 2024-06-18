#What is the 10001st prime number?

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def nth_prime(n):
    count = 0  # counting prime numbers
    num = 1    
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

nth= 10001
result = nth_prime(nth)

print(result)
