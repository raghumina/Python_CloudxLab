# while loop
# the loop which runs until the condition is true
'''
# for example
a = 10
while a < 20:
    print("yohooo")    # this loop will run infinitely because condition will never gonna be true
'''

#
a = 10
count = 0
while a < 20:  # now it runs until the provided condition gets true
    a = a + 1
    count = count + 1
    print(count, "yoho")

# this loop is similar to the for loop in many ways


##
# problem 1
# guess a number game
# lets start

num = 26
print("---------------------------Guess a number game----------------")
#print('''Rules :
1.You will get 10 chances to guess a number
2.The pop up will direct you or help you
3.If you cant guess in 10 chances the game will be over for you
#''')
print("Lets start")

print("If you want a hint Enter 'Yes'")
hint = str.upper(input("Enter 'Yes' or 'No': "))
if hint == "YES":
 #   print('''The number is a two digit number
    It is less than 41
 #   And greater than 10''')

num1 = int(input("Please enter the number you have guessed: "))
for num1 in range(9,42):


'''