# Dictionaries and tuples in python
p = "hello"
print(len(p))

names = ['harry', 'ron', 'guy', 'lee']
print("hello", names)
for names in names:
    print("happpy new year ", names)
print(list(names[0]))
print(len(names))
print(list(range(len(names))))

# dictionaries are pythons most powerful data collection
# allow us to do fast database like operations

# count values in a dictionary
# count = 0
count = dict()
names = {'mary', 'mary', 'hello', 'marry', 'tom', 'alex', 'tom'}
for names in names:
    if names not in count:
        count[names] = 1

# tuples can not be changed once declared
# for exampele

x = {1, 'tom', 2, 'jerry', 3, 'duck'}  # a tuple
type(x)
print(x)
print(type(x))

y = [1, 2, 3, 4, 'tom', 'jrry']  # a list
print(type(y))

# dictionary example
# dictionary is a kind of set of list but with no proper address so we have to give  a key to it

name = {'TOM': 'TOM@gmail.com', 'jerry': 'jerry@gamil.com'}
print(name['TOM'])  # it will return the mail of the TOM

for email in name:
    print(name)

# another example is that is
# python unpackaing
players = {'Ronaldo ', 'Messi', 'Kaka'}
realmadrid, Barcelona, Milan = players
print(Milan, Barcelona, realmadrid)
