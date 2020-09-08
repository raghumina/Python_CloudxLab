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

print(dict1["Class"])   # to access the class value
print(dict1.values())     # it will print all the value of the dictionary (key values )
print(dict1.keys())    # it will print all key names of the dictionary

print(dict1.popitem())    # it will show the last item of the dictionary
print(dict1.get("Roll number"))   # to get the roll number or required data 