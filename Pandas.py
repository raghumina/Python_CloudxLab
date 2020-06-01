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
