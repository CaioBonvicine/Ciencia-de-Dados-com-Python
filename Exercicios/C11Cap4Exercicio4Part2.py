import numpy as np

ds = np.loadtxt(r"C:\Users\Meu-PC\Documents\Python\DataSets\space.csv", 
                delimiter=';', 
                dtype=str, 
                encoding='utf-8')

ds_spacex = ds[ds[:,1] == 'SpaceX']
print(len(ds_spacex))
ds_custos = ds_spacex[:,6]
ds_custos = ds_custos.astype(float)
print(np.argmax(ds_custos))
print(ds_spacex[np.argmax(ds_custos)])