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

'''
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
