import numpy as np

arr1 = np.ones(8)
arr2 = np.random.randint(1, 9, 8)

arr_soma = arr1 + arr2


if np.sum(arr_soma) >= 40:
    arr = arr_soma.reshape(4, 2)
else:
    arr = arr_soma.reshape(2, 4)

print("Array:\n", arr)
