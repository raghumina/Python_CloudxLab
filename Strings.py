# Strings
# a program to find the length of a string
# for example
'''
name = "MESSI"
for i in range(0, 5):
    print(name[i])  # this will return the range of the name
print(len(name))

for num in range(0, 10):  # the range will check the numbers from 0,9
    print(num)


# how to count the each letter of the string

index = 0
name = "RONALDO"
while index < len(name):
    letter = name[index]
    print(index,letter)
    index = index + 1
print("\nCool functions and loops ")


# to count specific letter in the string
# with the help of loop
name = 'Penaldo'
count = 0
for letter in name:
    if letter == 'a':
        count = count + 1
        print(count)

'''
n = "tommy"
print(n[0:])  # the colon will counts all the string based on the location or number we have given to it
# more examples
sentence = "what are you doing tom"
print(sentence)
print(sentence[10:])  # it will count the print the string afer 10th location that means the
# output will be
# "ou doing tom"
# and a before colon means
print(sentence[:3])  # all the values or character before 3
# the output will be
#   "wha"

ord('a')
print(ord('a'))  # the ord is a way to find the ascii value of the characters and the letters or numbers
print(ord('5'))
# help('')  # for the help in the string cases

# the upper case and lower case in strings
name = "penaldo"
print(name.upper())  # it will convert all the letters in the upper case
name_1 = "MESSI"
print(name.lower())  # lower will convert al the letters in the lower case

#dir(name)  # ????
#print(dir(name))  # it will shows the methods

# lets use some of this methods
print("hello how are you ".split())  # it will split up all the words in the sentence

