# Functions
# Catching Exceptions
# Program 1
# Define a function with name except_func
# which takes one argument with name num and returns its multiplication with itself.
# If the argument passed during the function call is not valid for multiplication,
# return a str with content invalid number.
'''
def except_func(num):
    try:
        num = float(input("Enter a number:\n"))
        mult = num * num
        return mult
    except:
        print("invalid number ")
        num = float(input("Please enter a number:\n"))


except_func(2)

# Program 2
import math


def new_function(num):
    return (num * math.pi)


def void_function(num1, num2):
    print(new_function(math.pow(num1, num2)))


void_function(4.6, 7.3)


# program 3

def add(x, y, z):
    a = x + y + z
    return a


print(add(1, 2, 3))

# program 4
def do_math(a, b, kind='add'):
    if (kind == 'add'):  # if this condition is true then the output will be a + b other wise else condition will run
        return a + b
    else:
        return a - b


do_math(1, 2)

# program 5
# LABELED PARAMETERS IN FUNCTIONS
# For example

def add_num(x, y, z='None'):
    if z == 'None':
        return x + y
    else:
        return x + y + z


print(add_num(1, 2))
print(add_num(1, 2, 3))

# Revising the Function part
# program 6
def hello(Name):
    print("Hello")
    print("How are you ")

print(hello(), "Tom")

try:
    def add(x, y):
        print(x + y)
except:
    print("Please put integer number")

print(add(2, 3))
'''


# program 7
# Lets try a nest function

def calculator(num1, num2):
    print("Please write the another function ")


def add(num1, num2):
    print(num1 + num2)


def mult(num1, num2):
    print(num1 * num2)


def sub(num1, num2):
    print(num1 - num2)


def div(num1, num2):
    print(num1 / num2)


def mod(num1, num2):
    print(num1 % num2)


def pow(num1, num2):
    print(num1 ** num2)


print(calculator(2, 2))
print(add(2, 2), div(3, 5), pow(2, 2))   # this way we can use multi functions at a time


# Program 8
