import numpy as np

ds = np.loadtxt(r"C:\Users\Meu-PC\Documents\Python\DataSets\space.csv", 
                delimiter=';', 
                dtype=str, 
                encoding='utf-8')

empresas, contagem = np.unique(ds[:,1], return_counts=True)
for emp, qtd in zip(empresas, contagem):
    print(f"{emp}: {qtd}")