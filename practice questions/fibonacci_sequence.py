

# fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones


# program no 1 (=> it just prints the final value)

def fibonacci(n):

    #base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # intialize the first two fibonanic numbers
    a,b = 0 , 1

    # loop to calculate the nth fibanonic number

    for _ in range(2,n + 1):
        a,b = b, a + b

    return b

# example
n = 10
print(fibonacci(n))



# program no 2 (=> it  prints all previous values along with final value)

def fibonacci_2(n):
    # base case for n = 0 or n = 1

    if n == 0:
        print(0)
        return
    elif n == 1:
        print(0,1)
        return
    
    #intialize the first two fibonacci numbers

    a,b = 0,1

    fibonacci_sequence = [a,b] # stores fibonnacci numbers in a list

    # loop to calculate fibonacci numbers up to the nth number

    for _ in range(2, n + 1):
        a,b = b,a+b 
        fibonacci_sequence.append(b) # append the current fibonacci number
    

    # print all fibonacci numbers up to the nth
    print(fibonacci_sequence)


# example usage
n = 10
fibonacci_2(n)