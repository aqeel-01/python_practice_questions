
# program
'''
write a function to find the largest prime factor of a given number
'''

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

num = 56
print("largest prime factor of ", num , "is",largest_prime_factor(num))