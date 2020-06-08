# for and while loop
# the loop conditions

# A sample program
# program 1
# infinite loop
# i = 0
# while i < 12:     # this will print an infinite loop
#    print("hello")
#    print("raghu")
# print("ohoho")

# program 2
# another sample  program
# with break
# while True:
#    line = input(" >")
#    if line == 'done':
#        break  # break the loop when condition is met
#    print(line)
# print("Done ")

# program 3
# sample program
# with continue

#while True:
#    line = input(" >")
#    if line == '#':  # this will continue the loop
#        continue  # until the next condition is met
#   if line == 'done':
#       break
#       print(line)
'''
# program 4
#print('completed')
import turtle
while True:
    line = input("Please Enter your name\n ")
    line2 = int(input("Please enter your age\n"))
    line3 = input("Please enter your city ")
    line4 = int(input("Please enter your zip code"))
    if line4 == 302033:
        break
        print("You are from Rajasthan ")
        for steps in range(50):
            turtle.color("green")
            turtle.forward(100)
            turtle.right(90)
print("complete")
'''

# revision
# program 5
n = 5
while n > 0:
    print(n)
    n = n - 1
print("Ohk")
print(n)

