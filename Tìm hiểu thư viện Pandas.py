import pandas as pd
k = pd.read_csv('panda.csv')
print(k.head(10))
url='https://boris.unibe.ch/113257/15/taxreform.csv'
data = pd.read_csv(url,sep=';')
print(data.head(10))
url='https://api.github.com/users?since=100'
data = pd.read_json(url)
print(data.head(10))
