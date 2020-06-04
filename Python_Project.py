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