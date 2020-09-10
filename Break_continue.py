# Break and continue in python
# use to exit a while loop
# lets try a program
'''
for i in range(0, 100):
  #  if 1 == 1 or i == 2 or i == 99:
        #continue
    print(i)
'''

##
# problem 1
# guess a number game
# lets start

num = 26
print("---------------------------Guess a number game----------------")
print('''Rules :
1.You will get 10 chances to guess a number
2.The pop up will direct you or help you 
3.If you cant guess in 10 chances the game will be over for you 
''')
print("Lets start")

print("If you want a hint Enter 'Yes'")
hint = str.upper(input("Enter 'Yes' or 'No': "))
if hint == "YES":
    print('''The number is a two digit number 
    It is less than 41
    And greater than 10''')

num1 = int(input("Please enter the number you have guessed: "))


