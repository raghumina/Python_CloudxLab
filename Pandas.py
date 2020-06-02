# pandas is a library for data manipulation and analysis

'''
# import pandas as pd
import pandas as pd

pd.Series

animals = ['Lion', 'Tiger', 'Jaguar']
pd.Series(animals)
print(pd.Series(animals))

# Querying a series
sports = {'France': 'Football',
          'USA': 'Basketball',
          'India': 'Hockey',
          'China': 'Badminton'}

s = pd.Series(sports)
print(s)

# loc and iloc are attributes not methods
print(s.iloc[3])  # this attribute will lock the 3rd value in the sports series
print(s.loc['Hockey'])


# creation of data frames in python using the pandas library
import pandas as pd

# data frame data structures
player_1 = pd.Series({"Name": "Messi",
                      "Position": "Forward",
                      "Role": "Captain"})
player_2 = pd.Series({"Name": "Neymar",
                      "Position": "Left Winger",
                      "Role": "Attacker"})
player_3 = pd.Series({"Name": "Pique",
                      "Position": "Defender",
                      "Role": "Vice Captain"})
player_4 = pd.Series({"Name": "Sergio",
                      "Position": "Midfielder",
                      "Role": "Defensive Mid"})
df = pd.DataFrame([player_1, player_2, player_3, player_4], index = ['Attacker', 'Attacker', 'Defender', 'Midfilder'])
df.head()
print(df.head())

'''
# An another record
# sales record

import pandas as pd
purchase_1 = pd.Series ({'Shop':'Cothes',
                         'item_buy':'Shirt',
                         'Price':2500})
purchase_2 = pd.Series ({'Shop':'Toys',
                         'item_buy':'Car',
                         'Price':25})
purchase_3 = pd.Series ({'Shop':'Books',
                         'item_buy':'book',
                         'Price':250})
purchase_4 = pd.Series ({'Shop':'Cothes',
                         'item_buy':'Jeans',
                         'Price':25000})
purchase_5 = pd.Series ({'Shop':'Books',
                         'item_buy':'Novel',
                         'Price':350})
purchase_6 = pd.Series ({'Shop':'Cothes',
                         'item_buy':'Trousers',
                         'Price':1500})
purchase_7 = pd.Series ({'Shop':'Colors',
                         'item_buy':'Paint',
                         'Price':4570})
purchase_8 = pd.Series ({'Shop':'Stationary',
                         'item_buy':'Pens',
                         'Price':25})
purchase_9 = pd.Series ({'Shop':'Cothes',
                         'item_buy':'Jacket',
                         'Price':5000})
df = pd.DataFrame([purchase_1,purchase_2,purchase_3,purchase_4,purchase_5,purchase_6,purchase_7,purchase_8,purchase_9],
                  index = ['Clothes_Shop','Toy_Shop','Book_Shop','Clothes_Shop','Book_Shop','Clothes_Shop','Color_Shop',
                           'Stationary_Shop','Clothes_Shop'])

print(df)
# a data frame has been created


