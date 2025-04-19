


# program no 1
def find_largest_element(number):
    # intialize the first element as the largest
    largest = number[0]


    # iterate through the list to find the larget element

    for num in number:
        if num > largest:
            largest = num

    return largest

input_list = [3,1,4,5,6,74,2,5,35,7899,543,53]
print(find_largest_element(input_list))


# program no 2 , same but using sorting technique we find largets num

def largest_element(num):

    # sort the list in descending order (note => not in ascending )
    num.sort(reverse=True)

    # the larget number will be first element in the sorted list
    return num[0]

num = [3,1,4,6,3,6,3,54,6,42,5,7,7,33]

# call the function
print(largest_element(num))