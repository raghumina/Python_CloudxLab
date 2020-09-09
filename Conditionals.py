# if , else , elif are the conditional statements in the python
# they give the python power to analysis check the condition and give required output
'''
# so lets start
# lets check the greater number among the three numbers
num1 = int(input("Enter number 1:"))
num2 = int(input("Enter number 2:"))
num3 = int(input("Enter number 3:"))
if num1 > num2 and num1 > num3:
    print("Num1 is greatest")
elif num2 > num1 and num2 > num3:
    print("num2 is greatest ")
elif num1 == num2 and num1 == num3 and num2 == num3 and num2 == num1:
    print("all numbers are equal")
else:
    print("num3 is greatest ")
'''
# now lets create a condition for driving if age > 18 allowed to drive and if age < 18 not allowed and
# if age == 18 also allowed to drive
'''
age = int(input("Enter age here : "))
if age > 18:
    print("Allowed to drive")
elif age == 18:
    print("Allowed to drive")
else :
    print("Not allowed to drive ")
'''
# lets try another problem
# Take value of length and breadth and decide weather it is rectangle or not
'''
length = float(input("Enter length here : "))
breadth = float(input("Enter breadth here : "))

if breadth == length:
    print("It is a square")
elif breadth > length or breadth < length:    # we dont need this condition still i put it for fun :) :)
    print("this is rectange ")
'''
# another problem
# A shop will give discount of 10% if the cost of purchased price is more than 1000.
# Ask user for quantity
# Suppose, one unit will cost 100.
# Judge and print total cost for user
'''
quantity = int(input("Enter quantity here : "))
cost = 100 # for each quantity
if quantity*100 > 1000:
    print("the cost is", (quantity*100) - (.1*quantity*100))
'''

# the next problem is
#  company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask user for their salary and year of service and print the net bonus amount.

year_of_service = int(input("Enter years here : "))
salary = float(input("Enter salary here : "))
if year_of_service > 5:
    print("bonus is", .5 * salary)
elif year_of_service == 5:
    print("one more year till bonus")
else:
    print("no bonus")