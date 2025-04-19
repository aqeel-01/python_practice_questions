
#program
'''
write a program to find the second largest number in a list
'''

num = [4,1,7,3,11,5,7,2]

unique_num = list(set(num)) # removes the duplicates
unique_num.sort()
if len(unique_num) >= 2:
    second_largest = unique_num[-2]
    print("second largest number : ", second_largest)
else:
    print("Not enough unique elements")