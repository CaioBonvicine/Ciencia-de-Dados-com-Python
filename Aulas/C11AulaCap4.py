#Introdução ao NUMPY!
import numpy as np
#Numby é uma biblioteca open source em python, largamente utilizada para computação, tanto na ciencia quanto na engenharia.

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))  # Verificando o tipo do objeto
#este é um array unidimensional, ou seja, uma lista de elementos.

mtz = np.array([[1, 2, 3], [4, 5, 6]])
print(mtz)
print(type(mtz))  # Verificando o tipo do objeto
#este é um array bidimensional, ou seja, uma matriz de elementos.

arr2 = np.ones(10)
print(arr2)
#Cria um array unidimensional com 10 elementos, todos iguais a 1.

mtz2 = np.zeros((3, 4))
print(mtz2)
#Cria uma matriz 3x4 (3 linhas e 4 colunas) com todos os elementos iguais a 0.

#ARANGE
arr3 = np.arange(0, 20, 2)
print(arr3)
#Cria um array unidimensional com valores de 0 a 20, com passo de 2.

print(arr3.min) #imprimindo o menor vetor do array
print(arr3.argmin) #imprimindo o indice do menor vetor do array
print(arr3.max) #imprimindo o maior vetor do array
print(arr3.argmax) #imprimindo o indice do maior vetor do array


#Operações com arrays
arr4 = np.arange(9, 0, -1)
arr5 = np.arange(1, 10, 1)

print(arr4 + arr5)  # Soma elemento a elemento
print(arr4 - arr5)  # Subtração elemento a elemento
# para essas operações, os arrays devem ser do mesmo tamanho

arr6 = np.random.randint(30, 100, 10)
print(arr6)
#Gera um array unidimensional com 10 números inteiros aleatórios entre 30 e 100.

np.random.seed(10)
arr7 = np.random.randint(3, 10, 10)
print(arr7)
print(np.unique(arr7, return_counts=True))  # Imprime os valores únicos do array e a quantidade que de vezes que cada um aparece.
#Gera um array com 10 números inteiros aleatórios entre 3 e 10, com uma seed fixa para reprodutibilidade.
