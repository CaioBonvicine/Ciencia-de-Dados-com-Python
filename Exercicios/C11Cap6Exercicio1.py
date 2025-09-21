import pandas as pd
import matplotlib.pyplot as plt

ds = pd.read_csv(r"C:\Users\Meu-PC\Documents\Python\DataSets\paises.csv", 
                delimiter=';')

norte_america = ds[ds["Region"] == "NORTHERN AMERICA                   "]

plt.figure(figsize=(8,5))
plt.plot(norte_america["Country"], norte_america["Birthrate"], color = "blue", marker='o')
plt.plot(norte_america["Country"], norte_america["Deathrate"], color = "red", marker='o')

plt.title("Vermelho - Taxa de Mortalidade\nAzul - Taxa de Natalidade")
plt.xlabel("País")
plt.ylabel("Taxas")


plt.show()