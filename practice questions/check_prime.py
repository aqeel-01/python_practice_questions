


def is_prime(n):

    #handle base cases
    if n <= 1:
        return False
    
    #check divisibility from 2 to n-1

    for i in range(2,n):
        if n % i == 0:
            return False # if n is divisible by any other number b/w 2 and n-1 ,it's not prime
            
    
    return True # if no divisors were found, it's a prime number



print(is_prime(29))
print(is_prime(10))