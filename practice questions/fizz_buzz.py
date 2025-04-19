
# program which has custom range from 1 to 100
def fizz_buzz():
    for i in range (1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=", ")
        elif i % 3 == 0:
            print("Fizz" , end=", ")
        elif i % 5 == 0:
            print("Buzz", end=", ")
        else:
            print(i , end=", ")



fizz_buzz()

print("")
# program 2 , in which user give the proper the range
def fizz_buzz(start,end):
    for i in range (start, end + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=", ")
        elif i % 3 == 0:
            print("Fizz" , end=", ")
        elif i % 5 == 0:
            print("Buzz", end=", ")
        else:
            print(i , end=", ")



fizz_buzz(1,20)