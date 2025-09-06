import pandas as pd
import numpy as np


np.random.seed(10)

df = pd.DataFrame(
    index = ['A', 'B', 'C', 'D', 'E'],
    columns = ['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1,50,[5,4])
)

menor_30 = df[df['X'] < 30]['X']
print("Media na coluna X dos elementos menores que 30: " ,menor_30.mean())



print()

print("Media da linha D:", df.loc['D'].mean())
print("Soma da linha E:", df.iloc[4].sum())

print()

df_slice = df.loc[['A', 'B', 'E'], ['X', 'Y']]
print(df_slice)
print()
print("Soma das linhas:", df_slice.sum(axis = 1))
print()
print("Soma das colunas:", df_slice.sum(axis = 0))

