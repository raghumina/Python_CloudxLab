# for and while loop
# the loop conditions

# A sample program

# infinite loop
# i = 0
# while i < 12:     # this will print an infinite loop
#    print("hello")
#    print("raghu")
# print("ohoho")


# another sample  program
# with break
# while True:
#    line = input(" >")
#    if line == 'done':
#        break  # break the loop when condition is met
#    print(line)
# print("Done ")


# sample program
# with continue

#while True:
#    line = input(" >")
#    if line == '#':  # this will continue the loop
#        continue  # until the next condition is met
#   if line == 'done':
#       break
#       print(line)

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
