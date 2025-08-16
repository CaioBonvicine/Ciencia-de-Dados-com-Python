import numpy as np
arr1 = np.arange(0, 51, 2)
arr2 = np.arange(100, 50, -2)

concatene = np.concatenate((arr1, arr2))

print("Array:", np.sort(concatene))
