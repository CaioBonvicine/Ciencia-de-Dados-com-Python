import numpy as np

ds = np.loadtxt(r"C:\Users\Meu-PC\Documents\Python\DataSets\paises.csv", 
                delimiter=';', 
                dtype=str, 
                encoding='utf-8')

ds_america = ds[ds[:,1] == 'NORTHERN AMERICA                   ']
print(len(ds_america))
