# to find the square of the elements in a list
'''
list = [2,4,5]
for i in list:
    print(i ** 2)


# or to save list to another list

list1 = [2, 4, 5]
list2 = []
for i in list1:
    list2.append(i ** 2)

print(list2)
'''
# or with function

add =  int(input("Enter numbers here: "))
#list1 = []
#print(list1)
def list(add):
    if add not in list1:
        list1.append(add ** 2)
        print(list1)
