# conditional operators related questions
# write a program to prompt the user for hours and rate per hour to compute gross pay
'''
# lets start
# program 1
hours = float(input("Please enter the hours here\n"))
rate_per_hour = float(input("Please enter the rate here\n"))
gross_pay = hours * rate_per_hour
print("The gross pay is:",gross_pay)


# program 2
# another normal revision or practise program
# lets find a largest number among the three numbers given by the user
number1 = int(input("Please enter number1 here\n"))
number2 = int(input("Please enter number2 here\n"))
number3 = int(input("Please enter number3 here\n"))
if number1 > number2 and number1 > number3:
    print("Number1 is largest")
elif number2 > number1 and number2 > number3:
    print("Number2 is largest")
else:
    print("Number3 is largest ")
print("All are equal or condition not matched ")

# lets try to solve this same question with multiple if condiotion or any other possible way
# progrm 3
num1 = int(input("Please enter number1 here\n"))
num2 = int(input("Please enter number2 here\n"))
num3 = int(input("Please enter number3 here\n"))
if num1 > num2 and num1 > num3:
    print("Number1 is largest")
    if num2 > num3 and num2 > num1:
        print("Number2 is largest")
        if num3 > num1 and num3 > num2:
            print("Number3 is largest")
        else:
            print("All are equal ")
            # not giving suitable answer in unexpected condition
            # what to do ????

# program 4
# another same type of question
number = int(input("Please enter a number "))
if number > 10:
    print("greater")
if number < 10:
    print("smaller")
if number == 10:
    print("equal")
'''
# program 5
# lets make the program 1 more efficient or interactive
# the program 1 is about the rent hour and the gross pay

hours = float(input("Please enter the hours here\n"))
rent = float(input("Please enter the rate here\n"))
gross_pay = hours * rent
if gross_pay > 1000:
    print(gross_pay)
    print("Out of range ")
if gross_pay <= 1000:
    print(gross_pay)
    print("in range ")

print("Got it")

