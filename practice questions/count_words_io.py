

# program
'''
write a program to count the number of words in a text file
'''

filename = "example2.txt"

def count_words(filename):
    try:
        with open(filename,"r") as file:
            text = file.read()
            words = text.split()
            return len(words)
    except FileNotFoundError:
        return "file not found"



print("word count in file ", count_words(filename))