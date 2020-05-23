# Parameters and arguments
# functions
# parameters and arguments in functions


# problem 1:
# Write a function with name my_function which takes one argument with name number.
# Then, inside the function, write these statements,
# 1 - Store the number in a variable xyz
# 2 - Convert it into str and store it in xyz_str
# 3 - Concatenate cloudxlab to xyz_str
# 4 - print xyz_str
# Test your function by passing an argument 10. It should print 10cloudxlab.

def my_function(number):
    xyz = number
    xyz_str = str(number)
    xyz_str = xyz_str+"cloudxlab"
    print(xyz_str)
    my_function(10)
my_function(10)


# problem 2
# Define a function with name new_function that takes an argument num and returns its multiplication with π.
# Define a void function with the name void_function which takes two arguments num1 and num2
# which makes the call to new_function with an argument as num1 raised to the power of num2.
# Within the void_function print the value returned by the call.
# In a new cell, call void_function with arguments as 4.6 and 7.3.

