# while loop
# the loop which runs until the condition is true
'''
# for example
a = 10
while a < 20:
    print("yohooo")    # this loop will run infinitely because condition will never gonna be true


#
a = 10
count = 0
while a < 20:  # now it runs until the provided condition gets true
    a = a + 1
    count = count + 1
    print(count, "yoho")

# this loop is similar to the for loop in many ways

'''
##
# problem 1
# guess a number game
# lets start

number = 20
guess = int(input("Please enter a number: "))
for guess in range(10, 30):
    if guess == number:

        print("correct guess")
        continue
    elif guess >= 30:
        print("please guess a smaller number")
    elif guess <= 10:
        print("please guess a smaller number ")
