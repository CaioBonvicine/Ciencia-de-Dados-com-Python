import numpy as np

np.random.seed(10)
mtz = np.random.randint(1, 51, (4, 4))

print("Media das linhas:", np.mean(mtz, axis=1))
print("Média das colunas:", np.mean(mtz, axis=0))
print("Maior media das linhas:", np.max(np.mean(mtz, axis=1)))
print("Maior media das colunas:", np.max(np.mean(mtz, axis=0)))
print(np.unique(mtz, return_counts=True))
