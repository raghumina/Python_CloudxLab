# Functions
# Catching Exceptions

# Define a function with name except_func
# which takes one argument with name num and returns its multiplication with itself.
# If the argument passed during the function call is not valid for multiplication,
# return a str with content invalid number.

def except_func(num):
    try:
        num = float(input("Enter a number:\n"))
        mult = num * num
        return mult
    except:
        print("invalid number ")
        num = float(input("Please enter a number:\n"))


except_func(2)

import math


def new_function(num):
    return (num * math.pi)


def void_function(num1, num2):
    print(new_function(math.pow(num1, num2)))


void_function(4.6, 7.3)



