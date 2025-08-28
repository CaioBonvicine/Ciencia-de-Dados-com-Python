import numpy as np

ds = np.loadtxt(r"C:\Users\Meu-PC\Documents\Python\DataSets\paises.csv", 
                delimiter=';', 
                dtype=str, 
                encoding='utf-8')

ds_literacy = ds[1:,9].astype(float)

print(f"Media de alfabetização: {ds_literacy.mean()}")