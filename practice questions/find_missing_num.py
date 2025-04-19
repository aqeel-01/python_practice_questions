

# program to handle 1 missing number
def find_missing_numbers(nums):
    # calculate n based on the length of the list
    n = len(nums) + 1

    #calculate the sum of the numbers from 1 to n using the formula
    total_sum = n * (n + 1) // 2 # it will give integer (if / then it returns float)

    #calculate the sum of the numbers in the given list
    current_sum = sum(nums)

    # the missing number is the diff b/w the total sum and the current sum
    return total_sum - current_sum

nums = [1,2,4,5,6]
missing_number = find_missing_numbers(nums)
print("missing number : ", missing_number)
