# Try Except and Exception in python
# Exception Handling
# or error handling
# used where there is a high risk of run time error
'''
num1 = input("Enter a number: ")
num2 = input("Enter number: ")
try:
    sum = num1 + num2
    print(sum)
except:
    print("Give a numerical value")
'''
number1 = input("Enter number: ")


try:
    number1 = int(input("Enter number: "))
    number2 = int(input("Enter number: "))


except Exception:
    print("Last chance ")
    print("Pleasew enter int values in input")
    number1 = int(input("Enter number: "))
    number2 = int(input("Enter number: "))
    print("correct input")
