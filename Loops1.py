#  using more functions
# or checking more conditions using loops
# for example finding a specific number in a list
'''
found = False
for numbers in [12, 34, 464, 343, 23, 565, 78, 23, 23, 565, 454]:
    if numbers == 23:
        found = True
        print(found, numbers)
'''

# another example
# this time the value wiil be a string

found = False
for name in ["messi", "neymar", "vidal", "alonso", "messi1", "pique"]:
    if name == "messi":
        found = True
        print(found, name)
    else:
        print("please type the name of the G.O.A.T")
# there are total 6 names in the list
# so it will give this output
# output :
# True messi  # because it starts checking the list from 0 left to right so first is true and others are false
# please type the name of the G.O.A.T
# please type the name of the G.O.A.T
# please type the name of the G.O.A.T
# please type the name of the G.O.A.T
# please type the name of the G.O.A.T


# lets try an another example of this boolean conditions with user input
name = input("Please enter your name\n")
found = False
if name == "Messi":
    found = True
    print(found, name)
    print("correct right entery")
else:
    found = False
    print(found, "Please try again later ")

