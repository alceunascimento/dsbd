import sys
import numpy as np
import time
import matplotlib.pyplot as plt

from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

from sklearn.metrics import confusion_matrix
from sklearn.datasets import load_svmlight_file

from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB


def evaluate_classifiers(X_train, y_train, X_test, y_test, batchsize=1000):
    classifiers = {
        'KNN': KNeighborsClassifier(n_neighbors=3),
        'Logistic Regression': linear_model.LogisticRegression(),
        'Linear Discriminant Analysis': LinearDiscriminantAnalysis(),
        'GaussianNB': GaussianNB(),
        'BernoulliNB': BernoulliNB(),
        'MultinomialNB': MultinomialNB(),
    }

    results = {name: [] for name in classifiers}
    times = {}  # Dicionário para armazenar o tempo de classificação dos 58k exemplos de teste

    for size in range(batchsize, X_train.shape[0] + 1, batchsize):
        X_train_subset = X_train[:size].toarray()
        y_train_subset = y_train[:size]

        print(f"Tamanho da base de treinamento: {size}")
        for name, clf in classifiers.items():
            start_time = time.time()
            clf.fit(X_train_subset, y_train_subset)
            score = clf.score(X_test.toarray(), y_test)
            elapsed_time = time.time() - start_time
            print(f"Classificador: {name} | Acurácia: {score:.4f} | Tempo: {elapsed_time:.2f} segs.")
            results[name].append(score)

            # Predição dos dados de teste e tempo de classificação para 58.000 exemplos
            start_pred_time = time.time()
            y_pred = clf.predict(X_test.toarray())
            pred_time = time.time() - start_pred_time
            
            # Imprime a matriz de confusão para o classificador atual
            print(f"Matriz de Confusão para {name}:")
            cm = confusion_matrix(y_test, y_pred)
            print(cm)
            
            # Armazena o tempo de classificação no dicionário
            if size == X_train.shape[0]:  # Apenas para o último bloco de treinamento (todos os dados)
                times[name] = pred_time

    return results, times

def plot_results(results, batchsize, total_samples):
    # Função para plotar os resultados de acurácia em função do tamanho da base de treinamento.

    training_sizes = list(range(batchsize, total_samples + 1, batchsize))
    
    # Plotar o gráfico para cada classificador
    plt.figure(figsize=(10, 6))
    
    for name, scores in results.items():
        plt.plot(training_sizes, scores, label=name)
    
    # Configurações do gráfico
    plt.title('Desempenho dos Classificadores em Função do Tamanho da Base de Treinamento')
    plt.xlabel('Tamanho da Base de Treinamento (número de exemplos)')
    plt.ylabel('Acurácia na Base de Testes')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.show()

def print_classification_times(times):
    # Função para exibir os tempos de classificação em uma tabela.

    print("\nTabela de Tempos de Classificação (58.000 exemplos de teste):")
    print("{:<30} {:<15}".format('Classificador', 'Tempo (segundos)'))
    print("-" * 45)
    for classifier, time_taken in times.items():
        print("{:<30} {:<15.6f}".format(classifier, time_taken))

if __name__ == "__main__":
    # Carregar os dados
    print("Carregando dados...")
    X_train, y_train = load_svmlight_file('train.txt')
    X_test, y_test = load_svmlight_file('test.txt')

    # Avaliar os classificadores e coletar tempos de classificação
    results, times = evaluate_classifiers(X_train, y_train, X_test, y_test)

    # Plotar os resultados
    plot_results(results, batchsize=1000, total_samples=X_train.shape[0])

    # Exibir a tabela de tempos de classificação
    print_classification_times(times)
