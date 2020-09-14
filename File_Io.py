#  File IO in python
# file input and output
# file Io Basics

'''
"r" - Open a file for reading
"w" - Open a file for writing
"+" - Used to update a file means read and write both
"x" - creates a file if not exists
"a" - means append to add more content to a file
"t" - text mode used for files which have text data
"b" - binary mode used for file which have binary data

'''

# Lets create a text file with name python.txt
f = open("python.txt")      # here now we opened a file
content = f.read()         # use read() function to read the content of the file
print(content)

