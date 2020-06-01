# pandas is a library for data manipulation and analysis

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