
# program

'''
write a program to find the most frequent element in a given list
'''

from collections import Counter

number = [12,3,2,12,4,12,5,6,12,3,2,4,3,12]

freq = Counter(number) # create a dictionary with counts
most_commonn = freq.most_common(1) # get's the most frequent element
print("Most frequent element and occurence : ",most_commonn[0])
print("Most frequent element : ",most_commonn[0][0])