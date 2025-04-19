

# program

'''
write a program to find the common elements between two lists
'''

list1 = [1,2,3,4,5]
list2 = [4,5,6,7,8]

intersection = list(set(list1) & set(list2))
print("common elements ",intersection)