# conditional operators related questions
# write a program to prompt the user for hours and rate per hour to compute gross pay
'''
# lets start
hours = float(input("Please enter the hours here\n"))
rate_per_hour = float(input("Please enter the rate here\n"))
gross_pay = hours * rate_per_hour
print("The gross pay is:",gross_pay)

'''
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
    print("Number 3 is largest ")
print("Got your answer : ) : )")