import numpy as np

ds = np.loadtxt(r"C:\Users\Meu-PC\Documents\Python\DataSets\paises.csv", 
                delimiter=';', 
                dtype=str, 
                encoding='utf-8')

regioes, contagem = np.unique(ds[1:,1], return_counts=True)
for reg, qtd in zip(regioes, contagem):
    print(f"{reg}: {qtd}")