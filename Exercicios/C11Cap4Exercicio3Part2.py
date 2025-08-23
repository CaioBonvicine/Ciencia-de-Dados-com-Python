import numpy as np

ds = np.loadtxt(r"C:\Users\Meu-PC\Documents\Python\DataSets\space.csv", 
                delimiter=';', 
                dtype=str, 
                encoding='utf-8')

ds_missoes = ds[:, 2] 
ds_eua = np.sum(np.char.find(ds_missoes, "USA") >= 0)
print(ds_eua)