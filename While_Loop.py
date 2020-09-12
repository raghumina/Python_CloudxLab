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
number = 10
guesses = 8

while guesses < 8:
    input1 = int(input("Enter your number here: "))
    if input1 > number:

        print("Guess a smaller number")
    elif input1 < number:
        print("guess a smaller number")
    else:
        print("you won")
        print(guesses, "no of guesses you have taken ")
        break
    print(8 - guesses, "no of guesses left ")
    guesses = guesses + 1
if guesses > 8:
    print("game over ")
