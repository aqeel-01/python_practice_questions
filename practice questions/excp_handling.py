
#program
'''
write a program that handles exceptions while dividing two numbers
'''

try:
    num1 = 10
    num2 = 0
    result = num1 / num2
except ZeroDivisionError:
    print("Error: division by zero is not allowed...")
else:
    print("result: ", result)
finally:
    print("execution complete")