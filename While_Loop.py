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
num = 20
guesses = 1
while guesses <= 10:
    user_input = int(input("Enter number here: "))
    if user_input > num:
        print("Please guess a smaller number :")
    elif user_input < num:
        print("Please guess a bigger number ")
    else:
        print("you won")
        print(guesses,"number of guesses you took to win ")
        break
    print(10-guesses,"number of guesses left")
    guesses = guesses + 1

if guesses > 10:
    print("game over ")

