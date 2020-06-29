# we will use the open() function to read a file
# open returns a file handle

# lets try
import csv
'''
file = 'Customer.csv'

fields = []
rows = []

with open('Customer.csv', 'r') as csvFile:
    csvreader = csv.reader(csvFile)

    fields = next(csvreader)

    for rows in csvreader:
        rows.append(rows)

        print("Total number of rows %d" % (csvreader.line_num))  # to count the numbers of the rows in the csv file

# printing the field names
print("the field names are :" + ", ".join(fields for fields in fields))

# Printing the first five rows of the table (csv file )
for row in rows[:5]:
    for col in rows:
        print("%10s" % col)
        print("\n")

# files related problem
# Define a function with the name as file_read_func that takes the path of the file as an argument
# (assume it as str format).
# Your code should check whether the file exists or not with the given path.
# If there is no file at the given path, return -1, else return the sum of the lengths of all words in the file.
# Please note that your code should not count "\n" which is the newline character.
# Sample Input file -
#
# This is a sample file for testing for Python course for learners in CloudxLab.
#
# Sample output (which is the sum of the length of all the words)-
#
# 65

def file_read_func(path):
    try:
         with open('Customer.csv') as f:
             content = f.read()
             content = content.replace('\n','')
             list_of_words = content.split('')
             sum = 0
             for word in list_of_words:
                 sum = sum + len(word)
                 return sum
    except:
        return  -1

print(file_read_func('Customer.csv'))

'''
import csv
xfile = open("Customer.csv",)
for Customer in xfile:
    print(Customer)


