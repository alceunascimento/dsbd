import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Exemplo de criação de um DataFrame
dados = {
    'aluno': ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4', 'Aluno5', 'Aluno6'],
    'taxa_frequencia': [0.75, 0.85, 0.95, 0.70, 0.85, 0.85]  # Taxa de frequência como fração
}
df = pd.DataFrame(dados)


mean = df['taxa_frequencia'].mean()


# Definindo o estilo do gráfico
sns.set(style="whitegrid")

# Criando um histograma com uma linha de densidade
plt.figure(figsize=(10, 6))
sns.histplot(df['taxa_frequencia'], bins=10, kde=True, color='blue')

# Adicionando títulos e labels
plt.title('Distribuição da Taxa de Frequência dos Alunos')
plt.xlabel('Taxa de Frequência')
plt.ylabel('Número de Alunos')

# Mostrar o gráfico
plt.show()
