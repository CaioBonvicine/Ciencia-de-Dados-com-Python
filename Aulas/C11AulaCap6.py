import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5])
y = x * 2
y2 = y + 3

plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

#plt.subplot(1, 2, 1)
#plt.plot(x, y, marker='o', linestyle='--', color='b', linewidth=2, label='Linha 1')


#plt.subplot(1, 2, 2)
#plt.plot(x, y, marker='o', linestyle='--', color='r', linewidth=2, label='Linha 2')
#plt.show()


ds = pd.read_csv(r"C:\Users\Meu-PC\Documents\Python\DataSets\paises.csv", 
                delimiter=';')

print(ds.head(3))

#Extraindo os 6 maiores paises em area do mundo

maiores = ds.nlargest(6, 'Area (sq. mi.)')

print(maiores[['Country', 'Area (sq. mi.)']])

plt.scatter(maiores['Country'], maiores['Area (sq. mi.)'], color='g')
plt.show()

