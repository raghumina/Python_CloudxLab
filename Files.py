# we will use the open() function to read a file
# open returns a file handle

# lets try
import csv

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


