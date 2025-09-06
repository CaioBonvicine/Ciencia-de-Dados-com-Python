#Pandas!

import pandas as pd
import numpy as np

#setando indices e valores em panda
indices = ['a', 'b', 'c']
valores = [1, 2, 3]

serie = pd.Series(index=indices, data=valores)
print(serie)
print(type(serie))
print(serie['a'])

dic= {'a': 10, 'b' : 20, 'c': 30}

serie1 = pd.Series(dic)
print(serie1)
print(type(serie1))
print(serie1['a'])

dic2 = {'a': 10, 'b' : 20, 'd': 40}
serie2 = pd.Series(dic2)

print(serie1 + serie2)
print(serie1 - serie2)

print(serie1.add(serie2, fill_value = 0)) #fazendo soma e prencheenco elementos vazios/nulos com 0
print(serie1.sub(serie2, fill_value = 0)) #fazendo subtração e prencheenco elementos vazios/nulos com 0

np.random.seed(10)

df = pd.DataFrame(
    index = ['A', 'B', 'C', 'D', 'E'],
    columns = ['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1,50,[5,4])
)

print(df)
print(df.iloc[0:2, :])
print(df.loc[['A', 'B'], ['W', 'X', 'Y', 'Z']])
