import pandas as pd
df=pd.read_csv('C://Users/win11/Downloads/archive/diabetes.csv')
a = df['race'].replace('?', "Other")
df['race'] = a
df.to_csv('C://Users/win11/Downloads/archive/diabetesf.csv', index=False)
print(df)