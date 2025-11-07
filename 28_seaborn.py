import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Criando um dataframe com o pandas
data = {
    'Idade':   [22,   25,   27,   30,   35,   40,   45,   50],
    'Salario': [2200, 2500, 2700, 3000, 3500, 4000, 4500, 5000]   
}
df = pd.DataFrame(data)

# Criando um grafico de dispersão com Seaborn usando os dados do dataframe
sns.scatterplot(data=df, x='Idade', y='Salario', color='green')

# Adicionando titulos e rotulos
plt.title('Relacao entre idade e Salario')
plt.xlabel('Idade')
plt.ylabel('Salario')

# Exibindo o grafico
plt.show()