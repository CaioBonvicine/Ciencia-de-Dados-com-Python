import numpy as np
import matplotlib.pyplot as plt

ds = np.loadtxt(r"C:\Users\Meu-PC\Documents\Python\DataSets\space.csv", 
                delimiter=';',
                dtype=str,
                encoding='utf-8')

locais = ds[:,2]
companias = ds[:,1]


usa = np.char.find(locais, "USA") >= 0
china = np.char.find(locais, "China") >= 0


empresas_usa = np.unique(companias[usa])
empresas_china = np.unique(companias[china])


plt.figure(figsize=(8,5))
plt.bar("USA", len(empresas_usa), color="blue")
plt.bar("China", len(empresas_china), color="red")
plt.title("Empresas Espaciais")
plt.show()
