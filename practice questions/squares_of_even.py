
# program
'''
using list comprehensions, create a list of squares of even numbers from 1 to 30

'''

squares = [ x** 2 for x in range(1,31) if x % 2 == 0]
print("squares of even numbers from 1 to 20 ", squares)