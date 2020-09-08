# dictionary in python
# dictionaries are also like other data colletions like tuples list etc
# dictionaries are also unordered
# we can use different different data types in a dictionary
# we use {} in dictionaries
# dictionaries have keys which act as the address or location of the data

# lets create a sample dictionary
# for example

dict1 = {
    "Name": "Tom",
    "Class": 4,
    "Roll number": 343,
    "Subject": "PCB"
}

print(dict1)
# so a dictionary has been created with the key values

# most of the functions are similar to the other data types

print(dict1["Class"])  # to access the class value
print(dict1.values())  # it will print all the value of the dictionary (key values )
print(dict1.keys())  # it will print all key names of the dictionary

print(dict1.popitem())  # it will show the last item of the dictionary
print(dict1.get("Roll number"))  # to get the roll number or required data

# dictionary in a dictionary

orders = {
    "Tom": "Burger",
    "Jerry": "Pasta",
    "Doggo": "fries",
    "Looney": {"veg": "Pizza",
               "nonveg": "Chicken",
               "drink": "cola"
               }
}

print(orders["Looney"]["drink"])  # to specifiy the dictionary

# the key value in a dicitonary can be a list , tuple  and a dictionary
# lets try to make a list in a dictionary
food = {
    "lion": "deer",
    "deer": "grass",
    "beer": ["grass", "honey", "insects", "fruits"]
}

print(food)
print(food["beer"])  # cool so it worked

# to add items in a dictionary both key and its values

food["bat"] = "insects"
print(food)

# to remove a key and its value from  the dictionary

del food["bat"]
print(food)




