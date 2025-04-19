
# program
'''
write a program using a lambda function to sort a list of tuples based on the second element
'''

tuple_list = [(1,3),(3,2),(2,1)]
sorted_list = sorted(tuple_list, key=lambda x: x[1]) # as indexing in pyhton starts from 0 , so 
                                                     # we put 1 for our problem
print("sorted list based on second element: ", sorted_list)


# based on 3rd element
tuple_list = [(1,3,3),(3,2,1),(2,1,2)]
sorted_list = sorted(tuple_list, key=lambda x: x[2]) # index 3 algined with our problem 
print("sorted list based on second element: ", sorted_list)


