import numpy as np

# Criando um array Numpy (vetor)
arr = np.array([1, 2, 3, 4, 5])

print('Array Numpy:')
print(arr)

# Operações matematicas em arrays
print('\n Array multiplicando por 2:')
print( arr * 2 )

# Operação entre arrays
arr2 = np.array([10, 20, 30, 40, 50])
print('\nSomando duas arrays:')
print(arr + arr2)

# Criando uma matrix (2D)
matriz = np.array([[1, 2, 3],[4, 5, 6]])
print('\nMatrix 2x3:')
print(matriz)

# Soma e media da matriz
print('\nSoma de todos os elementos da matriz:')
print(np.sum(matriz))

print('\nMédia dos elementros da matriz:')
print(np.mean(matriz))

# Transposta da matriz
print('\nMatriz transposta:')
print(matriz.T)

# Gerando numeros aleatorios
print('\nNumeros aleatorios entre 0 e 1:')
print(np.random.rand(3, 3)) # Gera uma matriz de 3x3 com valores aleatorios

