import numpy as np

ds = np.loadtxt(r"C:\Users\Meu-PC\Documents\Python\DataSets\paises.csv", 
                delimiter=';', 
                dtype=str, 
                encoding='utf-8')

print(ds[1:,0])
print(ds[1:,1])
print(ds[1:,2])
print(ds[1:,3])