
# program 
'''
write a program that writes text to a file and then reads from it
'''

filename = "example.txt"

# write to the file
with open(filename,"w") as file:
    file.write("hello, this is just a simple text file . \n let's learn python file i/o concept")

# read from the file
with open(filename, "r") as file:
    content = file.read()
print("file content: ")
print(content)