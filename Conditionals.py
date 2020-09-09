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

length = float(input("Enter length here : "))
breadth = float(input("Enter breadth here : "))

if breadth == length:
    print("It is a square")
elif breadth > length or breadth < length:
    print("this is rectange ")

