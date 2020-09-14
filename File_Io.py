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
'''
# Lets create a text file with name python.txt
f = open("python.txt")      # here now we opened a file
content = f.read()         # use read() function to read the content of the file
print(content)
f.close()
'''
#  if i want to read this file as a binary file we will use "rb" means read as binary
# lets try this
'''
f = open("python.txt","rb")
content = f.read()
print(content)
f.close()
'''
# we can use read() to read the specific amount of content
# for example
'''
f = open("python.txt","r")
content = f.read(10)    # lets say read 10 space worth of content
print(content)          # it will only read the availablee data after that it will igonre the data 
f.close()
'''
# to read the content of the file line by line
# so lets start

f = open("python.txt")
count = 0
for line in f:
    count = count + 1
    #print(count,line)   # it applies \n by default which creates gapes between the lines so to remove this
    print(count,line,end="")  # worked fine
    