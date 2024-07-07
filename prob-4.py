## Q: largest palindrome that can be made from two 3-digit nums
## A palindrome is a word, sentence, verse, or even number that reads the same backward or forward.
## eg: Mum, 2002 etc.....

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def largest_palindrome_product():
    max_palindrome = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if is_palindrome(product) and product > max_palindrome:
                max_palindrome = product
    return max_palindrome

print(largest_palindrome_product())

##answer: 906609
