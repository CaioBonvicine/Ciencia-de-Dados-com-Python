import numpy as np

ds = np.loadtxt(r"C:\Users\Meu-PC\Documents\Python\DataSets\paises.csv", 
                delimiter=';', 
                dtype=str, 
                encoding='utf-8')

ds_lat = ds[ds[:,1] == 'LATIN AMER. & CARIB    ']
ds_renda = ds_lat[:,9]
ds_GPM = ds_renda.astype(float)
print(ds_lat[np.argmax(ds_GPM)] [0])