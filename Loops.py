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

while True:
    line = input(" >")
    if line == '#':  # this will continue the loop
        continue     # until the next condition is met
    if line == 'done':
        break
        print(line)

print('completed')




