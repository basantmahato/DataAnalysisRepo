import pandas as pd

data = {
  "Name": ['CHANDAN','BASANT','GOLDEN'],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df) 
print(df.loc[0])
