

def sum_of_digits(num):
    #convert the number to a string and sum the numbers
    return sum(int(digit) for digit in str(num))


input_number = 12345
output = sum_of_digits(input_number)
print(f"the sum of the digits of {input_number} is {output}")