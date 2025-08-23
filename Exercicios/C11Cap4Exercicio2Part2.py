import numpy as np

ds = np.loadtxt(r"C:\Users\Meu-PC\Documents\Python\DataSets\space.csv", 
                delimiter=';', 
                dtype=str, 
                encoding='utf-8')

ds_custos = ds[1:,6]
ds_custos = ds_custos.astype(float)
ds_validos = ds_custos[ds_custos > 0]
print(ds_validos.mean())