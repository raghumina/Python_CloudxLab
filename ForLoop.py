# for loops in python
# they are also conditional statements

# for example
count = 0
list1 = ["Messi", "Suarez", "Vidal", "Dembele", "Sergio", "Pique"]
# for palyers in list1:
#    count = count + 1
#    print(count, palyers)


# what id there is a lsit in a list so how can we access both items or data
# lets try
'''
season_goals = [["Messi", 50], ["Suarez", 30], ["Vidal", 5], ["Dembele", 17], ["Sergio", 2], ["Pique", 5]]
# for goals in season_goals:
#    print(goals)   # this will print it like a list
# we can  also called unpacking of list 
# the better way to do that is

for palyers, goals in season_goals:
    count = count + 1
    print(count, palyers, goals)
'''

# lets apply above program on dictionary
# data set will be same but converted to dictionary

season_goals = [["Messi", 50], ["Suarez", 30], ["Vidal", 5], ["Dembele", 17], ["Sergio", 2], ["Pique", 5]]

dict1 = dict(season_goals)
print(dict1)    # so it will show it as a dictionary as in key and value format
#

for players , goals in dict1.items():
    print(players,"scored", goals,"goals in 2021")          #
