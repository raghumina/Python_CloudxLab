# Python projct on Cloudxlab course
# Python project - Churn Emails
# i have used the cloudxlab dataset
# and solved the problem on cloudxlab jupytr account



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

# Project part 3
# Write a function find_email_sent_days which reads the file
# /cxldata/datasets/project/mbox-short.txt and categorizes each mail message by which day of the week the email was sent.
#
# To do this do the following:
#
# Open the file and read it line by line
# Look for lines that start with "From"
# For those lines which start from "From",
# then look for the third word and keep a running count of each of the days of the week.
# How do you find the day of the week, is an exercise for you.
# Note: You have to store the results in a dictionary. Only store those day of the week that exists.
# For Example, if there is no line for Mon then it should not be in the dictionary elements.
#
# At the end of the program return the contents of your dictionary (order does not matter)

def find_email_sent_days():
    daysdict = {}
    dayslist = []

    with open("/cxldata/datasets/project/mbox-short.txt") as f:
      for line in f:
        dayslist = line.split()
        if len(dayslist) > 3 and line.startswith('From'):
            day = dayslist[2]
            if day not in daysdict:
                daysdict[day] = 1
            else:
                daysdict[day] += 1
    return daysdict