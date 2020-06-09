# Python projct on Cloudxlab course
# Python project - Churn Emails
# project part 1
# Count the numbers of lines

# Define a function number_of_lines
# Open the file mbox-short.txt which is located at /cxldata/datasets/project/mbox-short.txt
# Read the file into one string by using read method on file handle
# Write logic to count the number of lines
# Return the count of the number of lines


def num_of_lines():
        fhand = open('/cxldata/datasets/project/mbox-short.txt')
        inp = fhand.read()
        fhand.close()
        count = 0
        for c in inp:
            if c == '\n':
                count += 1
        return count

# Project part 2
# Write a function count_number_of_lines which returns the count of the number of lines starting with Subject:
# in the file /cxldata/datasets/project/mbox-short.txt
# PS - If your logic is correct then your function should return 27.

def count_number_of_lines():
    with open('/cxldata/datasets/project/mbox-short.txt') as f:
        count = 0
        for line in f:
            line = line.rstrip() # Remove new line characters from right
            if line.startswith('Subject:'):
                count = count + 1
    return count

count_number_of_lines()

