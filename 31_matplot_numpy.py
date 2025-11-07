import matplotlib.pyplot as plt
import numpy as np

# Exemplo 01: Grafico de linha

# Dados para o grafico de linha
x = np.linspace(0, 10 , 100) # 100 pontos entre 0 e 10
y = np.sin(x) # Funcção seno

# Criando o grafico de linha
plt.plot(x, y, label='Seno(x)', color='b')

# Adicionando titulos e rotulos
plt.title('Grafico de linha: Seno(x)')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')

# Adicionar uma legenda
plt.legend()

# Exibir o grafico
plt.show()

# Exemplo 2: Grafico de barras

# Dados para o grafico de barras
categorias = ['A', 'B', 'C', 'D']
valores =    [ 10,  20,  15,  25]

#Criando o grafico de barras
plt.bar(categorias, valores, color = 'green')

# Adicionando rotulos e titulos
plt.title('Grafico de barras')
plt.xlabel('Categorias')
plt.ylabel('Valores')

#Exibindo o grafico
plt.show()