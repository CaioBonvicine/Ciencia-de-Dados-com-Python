import numpy as np

ds = np.loadtxt(r"C:\Users\Meu-PC\Documents\Python\DataSets\space.csv", 
                delimiter=';', 
                dtype=str, 
                encoding='utf-8')
print(len(ds))
ds_sucess = ds[ds[:,7] == 'Success']
print(len(ds_sucess))

print((len(ds_sucess) / len(ds)) * 100)