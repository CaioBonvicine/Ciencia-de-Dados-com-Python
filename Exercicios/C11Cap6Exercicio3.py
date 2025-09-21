import numpy as np
import matplotlib.pyplot as plt


ds = np.loadtxt(r"C:\Users\Meu-PC\Documents\Python\DataSets\space.csv", 
                delimiter=';',
                dtype=str,
                encoding='utf-8')

ds_roscomos = ds[ds[:,1] == 'Roscosmos']

ds_resultados = ds_roscomos[:,7]

sucesso_falha, cont = np.unique(ds_resultados, return_counts=True)

plt.figure(figsize=(8,5))
plt.pie(cont, labels=sucesso_falha, autopct='%1.1f%%', colors=['red', 'yellow', 'blue'])
plt.title("Resultados dos Lançamentos da Roscosmos")
plt.show()