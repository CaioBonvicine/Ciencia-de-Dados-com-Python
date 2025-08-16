import numpy as np


linhas = np.random.randint(3, 9)
colunas = np.random.randint(3, 9)

print(f"Número de linhas: {linhas}, Número de colunas: {colunas}")

mtz = np.random.randint(0, 1, (linhas, colunas))
print("Matriz:\n", mtz)


linhas_mtz, colunas_mtz = mtz.shape
total = linhas_mtz * colunas_mtz

if total % 2 == 0:
    print("Essa matriz pode ser transformada em um vetor unidimensional com número PAR de elementos.")
else:
    print("Essa matriz pode ser transformada em um vetor unidimensional com número ÍMPAR de elementos.")
